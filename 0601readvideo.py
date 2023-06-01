import cv2
video = cv2.VideoCapture("output_2.mp4")

while cv2.waitKey(1)!=27 : #按esc鍵
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("frame",frame)

    """if ret:
        cv2.imshow("frame",frame)
    else:
        break"""

video.release()
cv2.destroyAllWindows()

