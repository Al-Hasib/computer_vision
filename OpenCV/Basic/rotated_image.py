import numpy as np
import argparse
import immmm
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help = 'Path to the image file')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(3,3),0)
edged = cv2.Canny(blur,50,150)

cnts = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = immmm.grab_contours(cnts)

if len(cnts) > 0:
    c = max(cnts,key=cv2.contourArea)
    mask = np.zeros(gray.shape,dtype='uint8')
    cv2.drawContours(mask,[c],-1,255,-1)

    (x,y,w, h) = cv2.boundingRect(c)
    imageROI = img[y:y+h,x:x+w]
    maskROI = mask[y:y+h,x:x+w]
    imageROI = cv2.bitwise_and(imageROI, imageROI, mask = maskROI)
    for angle in np.arange(0,360,15):
        rotated = immmm.rotate(imageROI, angle)
        cv2.imshow("ROtated(Probmatic",rotated)
        cv2.waitKey(0)
    for angle in np.arange(0, 360, 15):
        rotated = immmm.rotate_bound(imageROI, angle)
        cv2.imshow("ROtated(Correct)", rotated)
        cv2.waitKey(0)

cv2.destroyAllWindows()


