import cv2
import numpy as np

img = cv2.imread('tetris.jpg')

def nothing(x):
    pass

#create a window
cv2.namedWindow('image')

# create trackbar for color Change
cv2.createTrackbar('lowH','image',0,179,nothing)
cv2.createTrackbar('highH','image',179,179,nothing)

cv2.createTrackbar('lowS','image',0,255,nothing)
cv2.createTrackbar('highS','image',255,255,nothing)

cv2.createTrackbar('lowV','image',0,255,nothing)
cv2.createTrackbar('highV','image',255,255,nothing)

while True:
    frame = img.copy()

    ilowH = cv2.getTrackbarPos('lowH','image')
    ihighH = cv2.getTrackbarPos('highH','image')

    ilowS = cv2.getTrackbarPos('lowS','image')
    ihighS = cv2.getTrackbarPos('highS','image')

    ilowV = cv2.getTrackbarPos('lowV','image')
    ihighV = cv2.getTrackbarPos('highV','image')

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_hsv = np.array([ilowH,ilowS,ilowV])
    higer_hsv = np.array([ihighH,ihighS,ihighV])

    mask = cv2.inRange(hsv,lower_hsv,higer_hsv)

    frame = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('org', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', frame)

    if cv2.waitKey(0) & 0XFF == ord('q'):
        break

cv2.destroyAllWindows()