import cv2
import imutils

img = cv2.imread('istockphoto-878155798-612x612.jpg ')


frame = img.copy()
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(5,5))
thresh = cv2.threshold(blur,235,255,cv2.THRESH_BINARY_INV)[1]
#cv2.imshow('th',thresh)
cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print(len(cnts))
for c in cnts:
    M = cv2.moments(c)
    area = cv2.contourArea(c)
    print(area)
    if M['m00'] == 0:
        M['m00'] = 0.001
    cX = int(M['m10']/M['m00'])
    cY = int(M['m01']/M['m00'])
    epsilon = 0.001 * cv2.arcLength(c,True)
    data = cv2.approxPolyDP(c,epsilon,True)
    hull = cv2.convexHull(data)

    x,y,w,h = cv2.boundingRect(hull)

    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)

    cv2.drawContours(img,[c],-1,(0,255,34),3)
    cv2.drawContours(img,[hull],-1,(255,0,0),3)

    cv2.imshow('Hand',img)

    cv2.waitKey(0)

cv2.destroyAllWindows()