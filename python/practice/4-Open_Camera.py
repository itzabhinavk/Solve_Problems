import cv2 

#opene the defacult webcam (0 = built-in camera)

cam = cv2.VideoCapture(0)
while True:

    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow("live camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()