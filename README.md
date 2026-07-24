# ⚡ Fit Connect | Next-Gen AI Fitness & Multi-User Sports Platform 🏋️‍♂️🧘‍♀️📍

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Computer%20Vision-orange?style=for-the-badge&logo=google&logoColor=white)](https://google.github.io/mediapipe/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![UI/UX](https://img.shields.io/badge/Design-Glassmorphism%20Cyberpunk-cyan?style=for-the-badge)](https://github.com/shivanshsenpai/Fitness_One)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

**Fit Connect** is a unified, high-performance web platform designed for fitness enthusiasts, athletes, and sports lovers. Built with a modern **Glassmorphic Dark Cyberpunk UI**, computer-vision pose detection, intelligent macronutrient estimation, geolocation mapping, and **real-time multi-user chat & buddy matching**, **Fit Connect** delivers a state-of-the-art interactive training experience.

---

## 🌟 Comprehensive Feature Set

### 1. 🧘‍♀️ Real-Time AI Yoga & Posture Verification Studio
- **Biometric Landmark Tracking**: Employs Google MediaPipe Pose and OpenCV to evaluate 33 full-body joint landmarks in real-time via camera feed.
- **Degree-Level Angle Guidance**: Calculates exact angular deviations (e.g. `Lift Right Arm UP by 27°`, `Tuck Left Knee IN by 15°`) and displays solid HUD text overlay.
- **Perfect Alignment Indicator**: Turns the camera HUD **BRIGHT EMERALD GREEN (`#4ADE80`)** when posture hits 100% target alignment.
- **Step-by-Step Execution Guides**: Interactive sidebar cards detailing angle target rules for *T-Pose*, *Tree Pose (Vrikshasana)*, *Warrior Pose (Virabhadrasana)*, *Downward Dog (Adho Mukha)*, and *Cobra Pose (Bhujangasana)*.

### 2. 🤝 Live Multi-User FitMatch & Real-Time Chat
- **Real-Time Active Visitor Tracking**: Flask heartbeat endpoint (`/api/user/heartbeat`) tracks live online visitors with a glowing **"ONLINE NOW"** badge.
- **Schedule-Based Partner Matching**: Matches users scheduling workouts during identical time slots.
- **Instant Match Connection**: Real-time connect requests (`/api/connect`) trigger a mutual match modal and unlock a private live room.
- **Real-Time Live Chat**: Asynchronous polling (`/api/chat/messages` and `/api/chat/send`) enables real-time messaging between multiple visitors across different browsers/devices.

### 3. 🧮 Smart Calorie & Protein Counter
- **Mifflin-St Jeor Biometric Engine**: Computes precise Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE).
- **Goal Customization**: Supports Weight Maintenance, Deficit (Weight Loss), and Surplus (Muscle Gain) objectives.
- **Macronutrient Distribution Gauges**: Animated progress bars showing exact daily targets for Protein, Carbohydrates, and Healthy Fats.

### 4. 🥗 Weekly Diet & Meal Planner
- **Customized Meal Schedules**: Generates 7-day structured nutrition schedules tailored to user-specified target calories and diet preferences (Vegan or Combined).
- **High-Contrast Printable Layout**: Clean printable meal dashboard with nutrient breakdown cards.

### 5. 🍲 High-Protein Recipe Suggester
- **Pantry Combination Engine**: Auto-filters compatible ingredient pairings (e.g., Chicken, Tofu, Eggs, Chickpeas, Mushrooms) to suggest customized high-protein recipes with macro breakdowns and step-by-step preparation guides.

### 6. 🗺️ Geolocation Sports & Gym Hub Maps
- **Interactive Sports Finder**: Locate nearby Badminton courts, Cricket pitches, Football grounds, Gyms, Volleyball courts, and Yoga studios on a dark-mode interactive map.

---

## 🔌 REST API Specification

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `POST /api/user/heartbeat` | `POST` | Registers or updates active online user profile (`id`, `name`, `age`, `timeSlot`, `last_seen`). |
| `GET /api/users/active` | `GET` | Returns list of all visitors online within the last 45 seconds. |
| `POST /api/connect` | `POST` | Records connection request between two users and returns a canonical `room_id`. |
| `POST /api/chat/send` | `POST` | Appends a new chat message into a live chat room. |
| `GET /api/chat/messages` | `GET` | Retrieves message history thread for a specific `room_id`. |
| `GET /video_feed` | `GET` | Streams OpenCV MediaPipe pose verification frames as MJPEG multipart response. |

---

## 🛠️ Technology Stack

| Component | Technologies & Frameworks |
| :--- | :--- |
| **Backend Engine** | Python 3.10+, Flask, OpenCV (`cv2`), MediaPipe Pose |
| **Frontend UI System** | HTML5, CSS3 Vanilla Design System (Glassmorphic Cards, Neon Cyberpunk Palette), JavaScript (ES6+ Async/Fetch) |
| **Real-Time Messaging** | Async REST API Polling & Local Storage Session Tracking |
| **Typography & Assets** | Google Fonts (*Outfit*, *Space Grotesk*), FontAwesome 6 Icons |

---

## 📁 Repository Hierarchy

```
Fitness_One/
├── app.py                     # Flask server, REST API endpoints & MediaPipe Pose engine
├── home.html                  # Landing page template with stats counter & feature grid
├── home.css                   # Core Design System tokens & home page styling
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
├── kl1.html                   # FitMatch Lobby user profile registration
├── kl.html                    # Live FitMatch Buddy cards deck & match overlay
├── kl.css                     # FitMatch card deck & live tag styling
├── chat.html                  # Real-time multi-user chat room interface
├── templates/
│   └── index.html             # AI Yoga Assistant live camera viewport & pose guides
└── logo.png, video.mp4, gifs  # High-definition media assets & graphics
```

---

## 🚀 Local Installation & Running Instructions

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

### Step 3: Run the Flask Application
```bash
python app.py
```

### Step 4: Access in Browser
Navigate to:
```
http://127.0.0.1:5000/
```

---

## 📜 Recent Update History

- **Multi-User Live Connect & Chat**: Built live REST API heartbeat, active user discovery (`/api/users/active`), and real-time message exchange (`/api/chat/send`, `/api/chat/messages`).
- **AI Camera Degree Guidance HUD**: Implemented exact joint angle correction feedback with solid dark slate banners and emerald green indicators.
- **Glassmorphism UI Overhaul**: Redesigned landing page, calorie calculator, diet planner, recipe suggester, and match cards.

---

## 📄 License
This project is open-source under the MIT License. Created by [Shivansh Senpai](https://github.com/shivanshsenpai).
