import cv2
import time
import numpy as np
import mediapipe as mp
import hand_tracking_module as htm
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def main():
    # --- CONFIGURATION ---
    W_CAM, H_CAM = 640, 480
    W_SCR, H_SCR = pyautogui.size()
    SMOOTH_ALPHA = 0.2  # EMA smoothing factor
    CLICK_DIST = 35     # Distance threshold for pinch-click
    CLICK_COOLDOWN = 0.5 # Seconds between clicks
    
    # --- INITIALIZATION ---
    cv2.namedWindow("Gesture Controller HUD", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Gesture Controller HUD", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    detector = htm.HandDetector(maxHands=1, detectionCon=0.85, trackCon=0.85)
    cap = cv2.VideoCapture(0)
    cap.set(3, W_CAM)
    cap.set(4, H_CAM)

    # Face Mesh Setup
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=False, min_detection_confidence=0.5)
    mp_draw = mp.solutions.drawing_utils
    drawing_spec = mp_draw.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 255))
    
    # Audio Setup
    devices = AudioUtilities.GetSpeakers()
    volume = devices.EndpointVolume
    vol_range = volume.GetVolumeRange()
    min_vol, max_vol = vol_range[0], vol_range[1]
    
    # State Vars
    prev_time = 0
    cloc_x, cloc_y = 0, 0
    ploc_x, ploc_y = 0, 0
    last_click_time = 0
    vol_bar, vol_per = 400, 0
    is_dragging = False
    drag_start_time = 0
    test_mode = False
    target_pos = (W_CAM // 2, H_CAM // 2)
    SMOOTH_DEADZONE = 5 
    R_CLICK_DIST, SCROLL_THRESHOLD = 40, 20
    prev_y_scroll = 0
    
    current_mode = "INITIALIZING..."

    while True:
        success, img = cap.read()
        if not success: break
        
        # 1. Face Mesh processing
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_results = face_mesh.process(img_rgb)
        if face_results.multi_face_landmarks:
            for face_landmarks in face_results.multi_face_landmarks:
                mp_draw.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=drawing_spec
                )

        # 2. Hand Detection
        img = detector.find_hands(img)
        lm_list = detector.find_position(img, draw=False)
        
        if len(lm_list) != 0:
            x_idx, y_idx = lm_list[8][1], lm_list[8][2]
            fingers = detector.fingers_up()
            
            # --- MODE: MOUSE ---
            if fingers[1] == 1 and fingers[2] == 0:
                current_mode = "MOUSE CONTROL"
                x_mouse = np.interp(x_idx, (100, W_CAM - 100), (0, W_SCR))
                y_mouse = np.interp(y_idx, (100, H_CAM - 200), (0, H_SCR))
                dx, dy = x_mouse - ploc_x, y_mouse - ploc_y
                if abs(dx) > SMOOTH_DEADZONE or abs(dy) > SMOOTH_DEADZONE:
                    cloc_x, cloc_y = ploc_x + dx * SMOOTH_ALPHA, ploc_y + dy * SMOOTH_ALPHA
                    pyautogui.moveTo(W_SCR - cloc_x, cloc_y)
                    ploc_x, ploc_y = cloc_x, cloc_y
                cv2.circle(img, (x_idx, y_idx), 15, (255, 0, 255), cv2.FILLED)

            # --- MODE: DRAG / CLICK ---
            if fingers[1] == 1 and fingers[0] == 1:
                length, img, line_info = detector.find_distance(4, 8, img)
                if length < CLICK_DIST:
                    if not is_dragging:
                        if drag_start_time == 0: drag_start_time = time.time()
                        if (time.time() - drag_start_time) > 0.4:
                            pyautogui.mouseDown(); is_dragging = True
                    current_mode = "DRAGGING" if is_dragging else "READY TO CLICK"
                    cv2.circle(img, (line_info[4], line_info[5]), 15, (0, 255, 0), cv2.FILLED)
                else:
                    if is_dragging: pyautogui.mouseUp(); is_dragging = False
                    elif drag_start_time != 0:
                        if (time.time() - drag_start_time) < 0.4: pyautogui.click()
                        drag_start_time = 0
            else:
                if is_dragging: pyautogui.mouseUp(); is_dragging = False
                drag_start_time = 0

            # --- MODE: RIGHT CLICK ---
            if fingers[2] == 1 and fingers[0] == 1:
                current_mode = "RIGHT CLICK"
                length, img, _ = detector.find_distance(4, 12, img)
                if length < R_CLICK_DIST:
                    if time.time() - last_click_time > CLICK_COOLDOWN:
                        pyautogui.rightClick(); last_click_time = time.time()

            # --- MODE: SCROLLING ---
            if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0:
                current_mode = "SCROLLING"
                if prev_y_scroll == 0: prev_y_scroll = y_idx
                diff = y_idx - prev_y_scroll
                if abs(diff) > SCROLL_THRESHOLD:
                    pyautogui.scroll(-int(diff * 2)); prev_y_scroll = y_idx
            else: prev_y_scroll = 0

            # --- MODE: VOLUME ---
            if all(f == 1 for f in fingers):
                length, img, _ = detector.find_distance(4, 8, img, draw=False)
                vol = np.interp(length, [30, 200], [min_vol, max_vol])
                vol_bar = np.interp(length, [30, 200], [400, 150])
                vol_per = np.interp(length, [30, 200], [0, 100])
                volume.SetMasterVolumeLevel(vol, None)
                current_mode = f"VOL CONTROL: {int(vol_per)}%"

        # UI: Top Status Bar
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        
        cv2.rectangle(img, (0, 0), (W_CAM, 60), (0, 0, 0), cv2.FILLED)
        cv2.line(img, (0, 60), (W_CAM, 60), (0, 255, 255), 2)
        cv2.putText(img, f"MODE: {current_mode}", (20, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f"FPS: {int(fps)}", (W_CAM - 150, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)

        # Accuracy Test HUD
        if test_mode:
            cv2.circle(img, target_pos, 20, (0, 255, 255), 2)
            cv2.putText(img, "ACCURACY TEST: REACH CENTER", (100, H_CAM-20, 150, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'): break
        elif key == ord('t'): test_mode = not test_mode

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
