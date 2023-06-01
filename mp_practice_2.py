import mediapipe as mp
import cv2

face_det = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def find_max(inputlist):
    maxValue = 0
    for m in inputlist:
        if m > maxValue:
            maxValue = m
    return maxValue

def find_min(inputlist):
    minValue = 1000
    for n in inputlist:
        if n < minValue:
            minValue = n
    return minValue 

img = cv2.imread("Lenna.jpg")
newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
FaceDetection = face_det.FaceDetection(model_selection=1)
result = FaceDetection.process(newimg)
#detection = result.detections[0]

if not result.detections:
    print("not people")
else:
    h,w,c = img.shape
    for detection in result.detections:
        xlist = []
        ylist = []
        for a in range(6):
            p= face_det.get_key_point(detection,a)
            xlist.append(p.x)
            ylist.append(p.y)

        min_x = int(find_min(xlist)*w)
        max_x = int(find_max(xlist)*w)
        min_y = int(find_min(ylist)*h)
        max_y = int(find_max(ylist)*h)

    #左上到右下(0,0)---(1,1)
    point1 = (min_x, min_y)
    point2 = (max_x, max_y)

    #point1 = (min_x, max_y)
    #point2 = (max_x, min_y)
    thickness = -1
    color = (0,255,0)
    cv2.rectangle(img,point1,point2,color,thickness) 

cv2.imshow("result",img)
cv2.waitKey(0)


"""xlist = []
ylist = []
for a in range(0,6):
    p = face_det.get_key_point(detection,a)
    xlist.append(p.x *w)
    ylist.append(p.y *h)

print(xlist)
max_x = int(max(xlist))
min_x = int(min(xlist))

max_y = int(max(ylist))
min_y = int(min(ylist))"""