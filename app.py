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

# Function to classify pose based on angles
def classifyPose(landmarks, output_image):
    label = "Unknown Pose"
    color = (0, 0, 255)

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

    # Calculate angles
    left_elbow_angle = calculateAngle(left_shoulder, left_elbow, left_wrist)
    right_elbow_angle = calculateAngle(right_shoulder, right_elbow, right_wrist)
    left_knee_angle = calculateAngle(left_hip, left_knee, left_ankle)
    right_knee_angle = calculateAngle(right_hip, right_knee, right_ankle)
    hip_angle = calculateAngle(left_shoulder, left_hip, left_knee)

    # Pose Detection Logic
    if 165 <= left_elbow_angle <= 195 and 165 <= right_elbow_angle <= 195:
        label = 'T Pose'
        color = (0, 255, 0)

    elif left_knee_angle < 100 or right_knee_angle < 100:
        label = 'Tree Pose'
        color = (255, 255, 0)

    elif (80 <= left_knee_angle <= 100 or 80 <= right_knee_angle <= 100) and \
         (165 <= left_elbow_angle <= 195 and 165 <= right_elbow_angle <= 195):
        label = 'Warrior Pose'
        color = (255, 165, 0)

    elif hip_angle > 150 and left_knee_angle > 150 and right_knee_angle > 150:
        label = 'Downward Dog'
        color = (0, 255, 255)

    elif 30 <= left_elbow_angle <= 60 and 30 <= right_elbow_angle <= 60 and hip_angle > 150:
        label = 'Cobra Pose'
        color = (255, 0, 255)

    elif abs(left_wrist[1] - left_ankle[1]) < 50 or abs(right_wrist[1] - right_ankle[1]) < 50:
        label = 'Triangle Pose'
        color = (0, 128, 255)

    # Display pose name
    cv2.putText(output_image, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

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
