import cv2
#from facemask import mosaic
from hand_detect import handpoint

video = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"DIVX") 
#out = cv2.VideoWriter("hand.mp4",fourcc,20.0,(640,480)) 

while cv2.waitKey(1)!=27:
    ret, frame = video.read()
    frame = handpoint(frame)
    cv2.imshow("frame", frame)
    #out.write(frame)

video.release()
#out.release()
cv2.destroyAllWindows()