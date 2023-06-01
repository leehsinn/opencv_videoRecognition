import mediapipe as mp
import cv2

face_det = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img = cv2.imread("Lenna.jpg")
newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
FaceDetection = face_det.FaceDetection(model_selection=1) #(多人參數)
result = FaceDetection.process(newimg)

if not result.detections:
    print("not people")
else:
    for result in result.detections:
        mp_drawing.draw_detection(img,result)
        print(result) #了解

    cv2.imshow("result",img)
    cv2.waitKey(0)

