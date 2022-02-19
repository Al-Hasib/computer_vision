import cv2
import numpy as np

def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),30,(0,23,1),2)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+150,y+50),(0,212,34),2)

cv2.namedWindow(winname='res')

img = np.ones([512,512,3]) * 255

cv2.setMouseCallback('res',draw)

while True:
    cv2.imshow('res',img)
    if cv2.waitKey(1) and 0XFF == 27:
        break
cv2.destroyAllWindows()