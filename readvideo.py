import cv2
from facemask import mosaic
from boundingmask import bound

x= int(input("輸入0或1"))
choose = []
choose.append(cv2.VideoCapture(0))
choose.append(cv2.VideoCapture("output_2.mp4"))
video = choose[x]


while cv2.waitKey(1)!=27 : #按esc鍵
    ret, frame = video.read()
    newframe = bound(frame)
    if not ret:
        break
    cv2.imshow("frame",newframe)


video.release()
cv2.destroyAllWindows()

