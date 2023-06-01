import mediapipe as mp
import cv2

mp_hand = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

#img = cv2.imread("hand_1.png")

def handpoint(img):

    newImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    handDetection = mp_hand.Hands()
    result = handDetection.process(newImg)
    if not result.multi_hand_landmarks:
        print("no hand")
    else:

        h,w,c = img.shape
        for hand_landmarks in result.multi_hand_landmarks:
            #hand_landmarks.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP]
            valX = hand_landmarks.landmark[8].x
            valY = hand_landmarks.landmark[8].y

            pixX = int(valX*w)
            pixY = int(valY*h)
            cv2.circle(img,(pixX,pixY),4,(0,0,255),-1)
    return img

#cv2.imshow("img",img)
#cv2.waitKey(0)