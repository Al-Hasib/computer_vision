import cv2
import numpy as np

img = np.zeros((300,512,3),np.uint8)
#img = cv2.imread('roi.png')
cv2.namedWindow("Color_picker")

def cross(x):
    pass

s1 = "0:OFF\n1:ON"
cv2.createTrackbar(s1,"Color_picker",0,1,cross)
cv2.createTrackbar("R","Color_picker",0,255,cross)
cv2.createTrackbar('G',"Color_picker",0,255,cross)
cv2.createTrackbar('B',"Color_picker",0,255,cross)

while True:
    cv2.imshow('Color_picker',img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    s = cv2.getTrackbarPos(s1,'Color_picker')
    r = cv2.getTrackbarPos("R",'Color_picker')
    g = cv2.getTrackbarPos('G','Color_picker')
    b = cv2.getTrackbarPos('B','Color_picker')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]

cv2.destroyAllWindows()

