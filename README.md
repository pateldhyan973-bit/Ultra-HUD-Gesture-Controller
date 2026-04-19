# 💎 Ultra-HUD Gesture Controller v2.0

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.11-green?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-red?style=for-the-badge)

A futuristic, high-performance Gesture Controller that allows you to control your Windows Desktop using your hands. Features an **Ultra-HUD** with real-time AI Face Mesh tracking and advanced OS-level interaction.

---

## 🌟 Features

- **🛸 Ultra-HUD Interface**: Futuristic Face Mesh contours and OSD (On-Screen Display) for Mode and FPS monitoring.
- **🖱️ Full Mouse Control**: Smooth, high-precision cursor movement with jitter-reduction.
- **👆 Advanced Gestures**: 
  - **Single Click**: Pinch Index & Thumb.
  - **Right Click**: Pinch Middle & Thumb.
  - **Drag & Drop**: Long-press Pinch.
  - **Vertical Scroll**: Two-finger swipe.
- **🔊 System Audio Control**: Adjust master volume with open-palm gestures.
- **🎯 Accuracy Test Mode**: Toggle a calibration target to test stability.

---

## 🖐️ Gesture Cheat Sheet

| Action | Hand Gesture | HUD Mode Label |
| :--- | :--- | :--- |
| **Move Cursor** | Index Finger Up | `MOUSE CONTROL` |
| **Left Click** | Pinch Index + Thumb | `READY TO CLICK` |
| **Drag & Drop** | Hold Pinch > 0.4s | `DRAGGING` |
| **Right-Click** | Pinch Middle + Thumb | `RIGHT CLICK` |
| **Scroll** | Index + Middle Up (✌️) | `SCROLLING` |
| **Volume** | Open Palm (All 5) | `VOL CONTROL` |

---

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/Ultra-HUD-Gesture-Controller.git
   cd Ultra-HUD-Gesture-Controller
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Controller**:
   ```bash
   python main.py
   ```

---

## ⌨️ Controls
- **'q'**: Quit the application.
- **'t'**: Toggle Accuracy Test Mode.

## ⚙️ Tech Stack
- **AI/ML**: MediaPipe (Hand Landmarking & Face Mesh)
- **Computer Vision**: OpenCV
- **OS Interaction**: PyAutoGUI, PyCaw, Comtypes
- **Language**: Python 3.x

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
