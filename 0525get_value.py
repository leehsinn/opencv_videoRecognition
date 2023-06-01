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
    h,w,c = img.shape

    for detection in result.detections: #result.detections是list
        p = face_det.get_key_point(detection,face_det.FaceKeyPoint.LEFT_EYE)
        print(p.x)
        print(p.y)
        pixelX = int(p.x *w)
        pixelY = int(p.y *h)
        cv2.circle(img,(pixelX,pixelY),3,(255,0,0),-1)

    cv2.imshow("result",img)
    cv2.waitKey(0)