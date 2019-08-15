import cv2
import numpy as np
import time

cap = cv2.VideoCapture("./Input.mp4")
time.sleep(4)
background = 0


ret, background = cap.read()

while (True):
    ret, img = cap.read()
    if ret == True and cv2.waitKey(1) != 27:
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        light1 = (0, 120, 70)
        dark1 = (10, 255, 255)
        mask1 = cv2.inRange(img_hsv, light1, dark1)

        light2 = (170, 120, 70)
        dark2 = (180, 255, 255)
        mask2 = cv2.inRange(img_hsv, light2, dark2)

        mask1 = mask1 + mask2

        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
        mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
        mask2 = cv2.bitwise_not(mask1)

        result1 = cv2.bitwise_and(background, background, mask=mask1)
        result2 = cv2.bitwise_and(img, img, mask=mask2)
        final_result = cv2.addWeighted(result1, 1, result2, 1, 0)

        cv2.imshow("final_result", final_result)

    else:
        break

cap.release()
cv2.destroyAllWindows()
