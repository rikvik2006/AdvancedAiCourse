import cv2

# 0 -> Droidcam
# 1 -> cam portatile
# 3 -> webcam usb
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:  # non è strettamente necessario testare
        # se l’acquisizione è andata a buon fine

        cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
