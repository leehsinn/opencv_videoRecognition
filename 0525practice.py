import mediapipe as mp
import cv2

face_det = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img = cv2.imread("blackpink_2.jpg")
newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
FaceDetection = face_det.FaceDetection(model_selection=1) #(多人參數)
result = FaceDetection.process(newimg)

if not result.detections:
    print("not people")
else:
    h,w,c = img.shape

    for detection in result.detections:
        print(detection)
        bounding = detection.location_data.relative_bounding_box
        
        
        p1= int((bounding.xmin)*w)
        p2= int((bounding.ymin+bounding.height)*h)

        q1= int((bounding.xmin+bounding.width)*w)
        q2= int((bounding.ymin)*h)

        point1 = (p1,p2)
        point2 = (q1,q2)

        thickness = 1
        color = (0,255,0)
        cv2.rectangle(img,point1,point2,color,thickness) 

    cv2.imshow("result",img)
    cv2.waitKey(0)