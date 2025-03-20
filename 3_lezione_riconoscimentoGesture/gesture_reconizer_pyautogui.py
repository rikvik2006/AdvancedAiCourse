import cv2
import math
import mediapipe as mp
import pyautogui
import subprocess
import time


def resize(image):
    DESIRED_HEIGHT = 480
    DESIRED_WIDTH = 480
    h, w = image.shape[:2]
    if h < w:
        img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h / (w / DESIRED_WIDTH))))
    else:
        img = cv2.resize(image, (math.floor(w / (h / DESIRED_HEIGHT)), DESIRED_HEIGHT))
    return img


BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

base_options = BaseOptions(
    model_asset_path="gesture_recognizer.task", delegate=BaseOptions.Delegate.CPU
)
options = GestureRecognizerOptions(
    base_options=base_options, running_mode=VisionRunningMode.VIDEO
)
recognizer = GestureRecognizer.create_from_options(options)

# 0 -> Droidcam portatile
# 1 -> cam portatile
# 3 -> webcam usb
cap = cv2.VideoCapture(0)

holding_mouse = False

while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", cv2.flip(frame, 1))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    recognition_result = recognizer.recognize_for_video(
        image, int(cap.get(cv2.CAP_PROP_POS_MSEC))
    )

    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()

    if recognition_result.gestures:
        segno = recognition_result.gestures[0][0]

        if segno.category_name == "Closed_Fist" and segno.score > 0.8:
            print("Apertura Paint")
            subprocess.run("mspaint")
            time.sleep(1)
        elif segno.category_name == "Pointing_Up" and segno.score > 0.8:
            pyautogui.moveRel(0, -1)
        elif segno.category_name == "Thumb_Up" and segno.score > 0.8:
            if not holding_mouse:
                pyautogui.mouseDown()
                holding_mouse = True
        elif segno.category_name == "Thumb_Down" and segno.score > 0.8:
            if holding_mouse:
                pyautogui.mouseUp()
                holding_mouse = False
        elif segno.category_name == "Victory" and segno.score > 0.8:
            pyautogui.moveRel(1, 0)
        elif segno.category_name == "ILoveYou" and segno.score > 0.8:
            pyautogui.moveRel(-1, 0)
        elif segno.category_name == "Open_Palm" and segno.score > 0.8:
            pyautogui.moveRel(0, 1)

recognizer.close()
cap.release()
cv2.destroyAllWindows()
