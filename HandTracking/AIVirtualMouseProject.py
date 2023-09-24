from cv2 import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui

#####################################

wCam, hCam = 640, 480
frameR = 100  # frame reduction
smoothening = 7

#####################################
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()
# print(wScr, hScr)

while True:
    # Find Hand Landmark
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # Get the tip of the index and middle finger
    if len(lmList) != 0:

        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # print(x1, y1, x2, y2)

    # check which finger are up
    fingers = detector.fingersUp()
    # print(fingers)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

    # only index finger i.e. moving mode
    if fingers[1] == 1 and fingers[2] == 0:

        # convert coordinate
        x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

        # smoothen values
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        # move mouse
        pyautogui.moveTo(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    # both index and middle fingers up : clicking mode
    if fingers[1] == 1 and fingers[2] == 1:

        # find distance between fingers
        length, img, lineInfo = detector.findDistance(8, 12, img)
        # print(length)

        # click mouse if distance short
        if length < 40:
            cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
            pyautogui.click()

    # frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.putText(img, "used index finger to control mouse ",
                (20, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

    # display
    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    if k == ord('c'):
        cv2.destroyAllWindows()
        # import menu
        break






