from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import math

# Initialize Flask app to serve from workspace root
app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)
mp_drawing = mp.solutions.drawing_utils

# Function to detect pose and extract landmarks
def detectPose(image, pose):
    output_image = image.copy()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(imageRGB)

    height, width, _ = image.shape
    landmarks = []

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(output_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        for landmark in results.pose_landmarks.landmark:
            landmarks.append((int(landmark.x * width), int(landmark.y * height), (landmark.z * width)))

    return output_image, landmarks

# Function to calculate angles between joints
def calculateAngle(landmark1, landmark2, landmark3):
    x1, y1, _ = landmark1
    x2, y2, _ = landmark2
    x3, y3, _ = landmark3

    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
    if angle < 0:
        angle += 360

    return angle

# Function to classify pose based on angles and generate real-time correction guidance
def classifyPose(landmarks, output_image):
    label = "Adjusting Position..."
    feedback = "Step into frame to align posture"
    color = (0, 165, 255) # Default Orange/Yellow

    if len(landmarks) == 0:
        return output_image, label

    # Extract key landmarks
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
    right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
    left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    right_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]
    left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
    right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]

    # Calculate joint angles
    left_elbow_angle = calculateAngle(left_shoulder, left_elbow, left_wrist)
    right_elbow_angle = calculateAngle(right_shoulder, right_elbow, right_wrist)
    left_knee_angle = calculateAngle(left_hip, left_knee, left_ankle)
    right_knee_angle = calculateAngle(right_hip, right_knee, right_ankle)
    hip_angle = calculateAngle(left_shoulder, left_hip, left_knee)

    # 1. T-Pose Classification & Corrections
    if (140 <= left_elbow_angle <= 210) and (140 <= right_elbow_angle <= 210) and (hip_angle > 140):
        if (165 <= left_elbow_angle <= 195) and (165 <= right_elbow_angle <= 195):
            label = "T POSE - PERFECT!"
            feedback = "PERFECT ALIGNMENT! (100% Correct)"
            color = (0, 255, 0) # GREEN when correct
        else:
            label = "T POSE - ALIGNING"
            color = (0, 215, 255) # Cyan/Yellow adjusting
            corrections = []
            if left_elbow_angle < 165:
                corrections.append(f"Lift Left Arm UP by {int(180 - left_elbow_angle)}deg")
            elif left_elbow_angle > 195:
                corrections.append(f"Lower Left Arm DOWN by {int(left_elbow_angle - 180)}deg")
            if right_elbow_angle < 165:
                corrections.append(f"Lift Right Arm UP by {int(180 - right_elbow_angle)}deg")
            elif right_elbow_angle > 195:
                corrections.append(f"Lower Right Arm DOWN by {int(right_elbow_angle - 180)}deg")
            feedback = " | ".join(corrections) if corrections else "Extend arms horizontally"

    # 2. Tree Pose (Vrikshasana) Classification & Corrections
    elif left_knee_angle < 110 or right_knee_angle < 110:
        bent_knee_angle = left_knee_angle if left_knee_angle < 110 else right_knee_angle
        straight_knee_angle = right_knee_angle if left_knee_angle < 110 else left_knee_angle
        bent_leg_name = "Left" if left_knee_angle < 110 else "Right"
        straight_leg_name = "Right" if left_knee_angle < 110 else "Left"

        if bent_knee_angle <= 90 and straight_knee_angle >= 160:
            label = "TREE POSE - PERFECT!"
            feedback = "EXCELLENT BALANCE! (100% Correct)"
            color = (0, 255, 0) # GREEN when correct
        else:
            label = "TREE POSE - ALIGNING"
            color = (0, 215, 255)
            corrections = []
            if bent_knee_angle > 90:
                corrections.append(f"Tuck {bent_leg_name} Knee IN by {int(bent_knee_angle - 80)}deg")
            if straight_knee_angle < 160:
                corrections.append(f"Straighten {straight_leg_name} Standing Leg by {int(175 - straight_knee_angle)}deg")
            feedback = " | ".join(corrections) if corrections else "Balance on single leg"

    # 3. Warrior Pose (Virabhadrasana)
    elif (70 <= left_knee_angle <= 110 or 70 <= right_knee_angle <= 110) and (150 <= left_elbow_angle <= 210):
        front_knee_angle = left_knee_angle if left_knee_angle <= 110 else right_knee_angle
        front_leg_name = "Left" if left_knee_angle <= 110 else "Right"

        if 85 <= front_knee_angle <= 95 and (165 <= left_elbow_angle <= 195):
            label = "WARRIOR POSE - PERFECT!"
            feedback = "STRONG STANCE! (100% Correct)"
            color = (0, 255, 0) # GREEN
        else:
            label = "WARRIOR POSE - ALIGNING"
            color = (0, 215, 255)
            if front_knee_angle > 95:
                feedback = f"Deepen {front_leg_name} Knee Bend DOWN by {int(front_knee_angle - 90)}deg"
            elif front_knee_angle < 85:
                feedback = f"Extend {front_leg_name} Knee OUT by {int(90 - front_knee_angle)}deg"
            else:
                feedback = "Keep arms level with shoulders"

    # 4. Downward Dog (Adho Mukha Svanasana)
    elif hip_angle > 140 and left_knee_angle > 140 and right_knee_angle > 140:
        if hip_angle >= 160:
            label = "DOWNWARD DOG - PERFECT!"
            feedback = "PERFECT V-SHAPE INVERT! (100% Correct)"
            color = (0, 255, 0) # GREEN
        else:
            label = "DOWNWARD DOG - ALIGNING"
            color = (0, 215, 255)
            feedback = f"Push Hips UP & Back by {int(170 - hip_angle)}deg"

    # 5. Cobra Pose (Bhujangasana)
    elif 25 <= left_elbow_angle <= 65 and 25 <= right_elbow_angle <= 65:
        if 35 <= left_elbow_angle <= 55:
            label = "COBRA POSE - PERFECT!"
            feedback = "CHEST LIFTED PERFECTLY! (100% Correct)"
            color = (0, 255, 0) # GREEN
        else:
            label = "COBRA POSE - ALIGNING"
            color = (0, 215, 255)
            feedback = f"Adjust Elbow Arch by {int(abs(45 - left_elbow_angle))}deg"

    # Render HUD overlay on video frame
    h, w, _ = output_image.shape
    
    # Top Status Box Banner
    cv2.rectangle(output_image, (10, 10), (w - 10, 60), (10, 15, 25), -1)
    cv2.rectangle(output_image, (10, 10), (w - 10, 60), color, 2)
    cv2.putText(output_image, label, (25, 43), cv2.FONT_HERSHEY_SIMPLEX, 0.85, color, 2)

    # Bottom Feedback Banner
    cv2.rectangle(output_image, (10, h - 60), (w - 10, h - 10), (10, 15, 25), -1)
    cv2.rectangle(output_image, (10, h - 60), (w - 10, h - 10), (255, 255, 255), 1)
    cv2.putText(output_image, f"GUIDANCE: {feedback}", (25, h - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

    return output_image, label

# Function to stream video frames
def gen():
    camera_video = cv2.VideoCapture(0)

    while True:
        ok, frame = camera_video.read()
        if not ok:
            continue

        frame = cv2.flip(frame, 1)
        frame, landmarks = detectPose(frame, pose_video)

        if landmarks:
            frame, _ = classifyPose(landmarks, frame)

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera_video.release()

# Flask Routes serving frontend files from workspace root
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calorie-calc')
def calorie_calc():
    return render_template('Calorie_Calc.html')

@app.route('/diet-chart')
def diet_chart():
    return render_template('dietChart.html')

@app.route('/recipes')
def recipes():
    return render_template('Recipes.html')

@app.route('/explore')
def explore():
    return render_template('maps_1.html')

@app.route('/explore/gym')
def explore_gym():
    return render_template('mapsGym.html')

@app.route('/explore/yoga')
def explore_yoga():
    return render_template('mapsYoga.html')

@app.route('/explore/badminton')
def explore_badminton():
    return render_template('mapsBadminton.html')

@app.route('/explore/cricket')
def explore_cricket():
    return render_template('mapsCrirkcet.html')

@app.route('/explore/football')
def explore_football():
    return render_template('mapsFootball.html')

@app.route('/explore/volleyball')
def explore_volleyball():
    return render_template('mapsVolleyball.html')

@app.route('/find-friends')
def find_friends():
    return render_template('kl1.html')

@app.route('/find-friends/matches')
def find_friends_matches():
    return render_template('kl.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/yoga-detection')
def yoga_detection():
    return render_template('templates/index.html')

@app.route('/run-python')
def run_python():
    # Legacy endpoint mock response to prevent Javascript errors
    return jsonify({'result': 'Chat loaded locally in browser'})

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
