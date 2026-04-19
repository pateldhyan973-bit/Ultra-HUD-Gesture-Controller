# <div align="center">💎 ULTRA-HUD: The Future of Desktop Interactivity</div>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Powered%20By-MediaPipe-blue?style=for-the-badge" alt="MediaPipe">
  <img src="https://img.shields.io/badge/Interface-Full--Screen-magenta?style=for-the-badge" alt="Interface">
  <img src="https://img.shields.io/badge/OS-Windows-0078D6?style=for-the-badge&logo=windows" alt="Windows">
</p>

---

## 📖 Table of Contents
1. [Overview](#-overview)
2. [Ultra-HUD Features](#-ultra-hud-features)
3. [The Gesture Library](#-the-gesture-library)
4. [Technology Stack](#-technology-stack)
5. [Installation](#-installation)
6. [Advanced Configuration](#-advanced-configuration)
7. [Roadmap](#-roadmap)

---

## 🛸 Overview
**ULTRA-HUD** is a next-generation gesture-based controller that turns your webcam into a high-precision input device. Unlike simple trackers, Ultra-HUD uses a dual-model AI stack to provide both **Gesture Command Execution** and a **Futuristic Face Mesh Overlay**, creating an immersive "Iron Man" style desktop experience.

> [!TIP]
> This tool is perfect for presentations, media centers, accessibility, or simply navigating your PC while your hands are busy.

---

## 💎 Ultra-HUD Features

### 📡 Dual-Model AI Engine
- **Face Mesh Tracker**: 468-point facial landmarking (Contours Mode) for immersive HUD feedback.
- **Hand Kinematics**: 21-point geometric hand tracking with real-time gesture classification.

### 🖥️ OSD (On-Screen Display)
- **Mode Indicator**: Persistent top-bar HUD showing real-time system state.
- **Performance Monitor**: Integrated FPS counter for latency tracking.
- **Calibration Target**: Built-in `Accuracy Test` mode for finding your optimal control distance.

---

## 🖐️ The Gesture Library

| Icon | Action | Gesture | HUD Mode |
| :---: | :--- | :--- | :--- |
| 🖱️ | **Move Mouse** | **Index Finger Up** | `MOUSE CONTROL` |
| 🔘 | **Left Click** | **Index + Thumb Pinch** | `CLICK` |
| 📦 | **Drag & Drop** | **Hold Pinch (>0.4s)** | `DRAGGING` |
| 📋 | **Right Click** | **Middle + Thumb Pinch** | `RIGHT CLICK` |
| 📜 | **Scroll** | **Index + Middle Up (✌️)** | `SCROLLING` |
| 🔊 | **Volume** | **Full Open Palm** | `VOL CONTROL` |

---

## ⚙️ Technology Stack
- **AI Core**: `MediaPipe 0.10.11` (Restored Solutions API)
- **Vision Logic**: `OpenCV 4.8` (Full-Screen WND Control)
- **OS API**:
  - `PyAutoGUI`: Cross-platform input simulation.
  - `PyCaw`: Windows core audio integration.
  - `Comtypes`: Low-level COM interface management.
- **Math Engine**: `NumPy < 2.0` (Native C-Optimized Arrays)

---

## 🛠️ Installation

### Prerequisites
- **Python 3.8+**
- **Webcam** (720p recommended)

### Quick Start
1. **Clone the Repo**
   ```bash
   git clone https://github.com/YourUsername/Ultra-HUD.git
   cd Ultra-HUD
   ```

2. **Run the Automatic Rebuild** (Ensures dependency stability)
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Launch Ultra-HUD**
   ```bash
   python main.py
   ```

---

## 🎯 Advanced Configuration
You can fine-tune the experience in `main.py`:
- `SMOOTH_ALPHA`: Increase for more stability, decrease for faster response.
- `CLICK_DIST`: Adjust the pinch sensitivity based on your hand size.
- `SMOOTH_DEADZONE`: The "Jitter Guard" range (in pixels).

---

## 🗺️ Roadmap
- [ ] **Dual Hand Support**: Independent control for left and right hands.
- [ ] **Custom Gesture Training**: Allow users to record their own gestures.
- [ ] **App-Specific Profiles**: Custom shortcuts for Chrome, VLC, and Gaming.
- [ ] **Eye-Tracking Navigation**: Combine face mesh with eye gaze.

---

## 📝 License
Built with passion by **Antigravity**. Licensed under the [MIT License](LICENSE).
