# Fit Connect | Next-Gen AI Fitness & Sports Platform 🏋️‍♂️🧘‍♀️📍

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Computer%20Vision-orange?style=for-the-badge&logo=google&logoColor=white)](https://google.github.io/mediapipe/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![UI/UX](https://img.shields.io/badge/Design-Glassmorphism%20Cyberpunk-cyan?style=for-the-badge)](https://github.com/shivanshsenpai/Fitness_One)

**Fit Connect** is a unified, high-performance web platform designed for fitness enthusiasts, athletes, and sports lovers. Powered by computer-vision pose detection, intelligent macronutrient estimation, geolocation mapping, and peer-to-peer buddy scheduling, **Fit Connect** delivers a state-of-the-art interactive training experience.

---

## 🌟 Key Features

### 1. 🧘‍♀️ Real-Time AI Yoga & Posture Coach
- **Computer Vision Verification**: Uses MediaPipe Pose and OpenCV to track 33 key biometric landmarks in real-time via camera feed.
- **Degree-Level Guidance & Green Indicator**: Calculates exact joint angle deviations (e.g. `Lift Right Arm UP by 27°`), turning **BRIGHT GREEN** when 100% pose alignment is achieved.
- **Step-by-Step Pose Guides**: Interactive UI cards for *T-Pose*, *Tree Pose*, *Warrior Pose*, *Downward Dog*, and *Cobra Pose*.

### 2. 🧮 Smart Calorie & Protein Counter
- **Mifflin-St Jeor Equation**: Computes precise Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE).
- **Goal Customization**: Supports Weight Maintenance, Deficit (Weight Loss), and Surplus (Muscle Gain) objectives.
- **Macronutrient Breakdown**: Visual progress bars displaying optimal Protein, Carbohydrate, and Healthy Fat intake.

### 3. 🥗 Weekly Diet & Meal Planner
- **Customized Meal Schedules**: Generates 7-day structured meal plans tailored to user-specified target calories and diet preferences (Vegan or Combined).
- **Printable Dashboard**: High-contrast, printable meal guide with progress gauges for energy and protein targets.

### 4. 🍲 High-Protein Recipe Suggester
- **Pantry Combination Engine**: Auto-filters compatible ingredient pairings (e.g., Chicken, Tofu, Eggs, Chickpeas, Mushrooms) to suggest customized high-protein recipes with macro breakdowns and step-by-step preparation guides.

### 5. 🗺️ Geolocation Sports & Gym Hub Maps
- **Interactive Sports Finder**: Locate nearby Badminton courts, Cricket pitches, Football grounds, Gyms, Volleyball courts, and Yoga studios on a dark-mode interactive map.

### 6. 🤝 Live Multi-User FitMatch & Real-Time Chat
- **Live Online Visitor Tracking**: Heartbeat API (`/api/user/heartbeat`) tracks online visitors in real-time with a glowing **"ONLINE NOW"** badge.
- **Instant Match & Live Chat**: Connect with online athletes, send match invites, and exchange real-time messages via Flask REST API endpoints (`/api/chat/send` and `/api/chat/messages`).

---

## 🛠️ Technology Stack

| Component | Technologies Used |
| :--- | :--- |
| **Backend Framework** | Python 3.10+, Flask, OpenCV (`cv2`), MediaPipe |
| **Frontend UI/UX** | HTML5, CSS3 Vanilla Design System (Glassmorphism, Neon Cyberpunk Theme), JavaScript (ES6+) |
| **Typography & Icons** | Google Fonts (*Outfit*, *Space Grotesk*), FontAwesome 6 |
| **Mapping & Visuals** | Embedded OpenStreetMap Geolocation, Custom SVG / Spline 3D typography |

---

## 📁 Repository Structure

```
Fitness_One/
├── app.py                     # Flask server application & MediaPipe Pose engine
├── home.html                  # Landing page template with stats & feature cards
├── home.css                   # Core Design System tokens & home styling
├── Calorie_Calc.html          # Calorie & Protein Calculator interface
├── Calorie_calc.css           # Calculator card styling & macro progress bars
├── dietChart.html             # Weekly Diet Planner dashboard
├── dietChart.css              # Diet chart styling & printable layout
├── Recipes.html               # Smart Recipe Suggester UI
├── recipes.css                # Recipe card grid styling
├── recipes.js                 # Dynamic recipe database & filter logic
├── maps_1.html                # Main Sports Mapping category lobby
├── maps_1.css                 # Mapping lobby styling
├── mapsGym.html               # Category specific map views (Gym, Yoga, etc.)
├── Maps.css                   # Embedded map dark theme styling
├── kl1.html                   # FitMatch Lobby input form
├── kl.html                    # FitMatch Buddy cards & match overlay
├── kl.css                     # FitMatch card deck styling
├── chat.html                  # Peer-to-peer buddy chat room interface
├── templates/
│   └── index.html             # AI Yoga Assistant live camera viewport
└── logo.png, video.mp4, gifs  # High-definition media assets & graphics
```

---

## 🚀 Local Setup & Running Instructions

### Prerequisites
- Python 3.9+ installed
- Webcam connected (for AI Pose Detection feature)

### Step 1: Clone Repository
```bash
git clone https://github.com/shivanshsenpai/Fitness_One.git
cd Fitness_One
```

### Step 2: Install Dependencies
```bash
pip install flask opencv-python mediapipe
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access in Browser
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 📄 License
This project is open-source under the MIT License. Created by [Shivansh Senpai](https://github.com/shivanshsenpai).
