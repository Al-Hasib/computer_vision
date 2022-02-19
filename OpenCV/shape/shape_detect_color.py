# Here, I will detect the shape and it's color

import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help = 'path of the image')

args = vars(ap.parse_args())



def detect_shape(contour):
    shape = 'undefined'
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.04*peri,True)

    if len(approx) ==3:
        shape = 'triangle'
    elif len(approx)==4:
        (x,y,w,h) = cv2.boundingRect(approx)
        ar = w/float(h)

        shape = 'square' if ar>=0.95 and ar<=1.05 else 'rectangle'

    elif len(approx)==5:
        shape = 'pentagon'
    elif len(approx)==6:
        shape= 'hexagon'
    else:
        shape = 'circle'
    return shape


img = cv2.imread(args['image'])
resized = imutils.resize(img,width= 350)
ratio = img.shape[0]/float(resized.shape[0])

gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blurred,200,255,cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    M = cv2.moments(c)
    cX = int((M['m10']/M['m00']) * ratio)
    cY = int((M['m01']/M['m00']) * ratio)

    shape = detect_shape(c)

    c = c.astype('float')
    c *= ratio
    c = c.astype('int')

    cv2.drawContours(img,[c],-1,(0,255,5),2)
    cv2.putText(img,shape,(cX,cY),cv2.FONT_HERSHEY_PLAIN,0.6,
                (255,255,23),2)
    cv2.imshow('image',img)
    cv2.waitKey(0)
cv2.destroyAllWindows()

