import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help = 'path of the image')

args = vars(ap.parse_args())

img = cv2.imread(args['image'])

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.threshold(blur,200,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow('image', thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_L1)
cnts = imutils.grab_contours(cnts)
print(len(cnts))

def center_shape(img,cnt):
    for c in cnt:
        M = cv2.moments(c)
        if M['m00'] == 0:
            M['m00'] = 0.001
        cX = int(M['m10']/M['m00'])
        cY = int(M['m01']/M['m00'])
        cv2.drawContours(img, [c], -1, (0, 23, 23), 3)
        cv2.circle(img, (cX, cY), 5, (0, 0, 0), -1)

def shape_detection(img,cnt):
    for c in cnt:
        M = cv2.moments(c)
        if M['m00'] == 0:
            M['m00'] = 0.001
        cX = int(M['m10']/M['m00'])
        cY = int(M['m01']/M['m00'])
        shape = 'Undefined'
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.04*peri,True)
        if len(approx) == 3:
            shape = 'triangle'
        elif len(approx) == 4:
            (x,y,w,h) = cv2.boundingRect(approx)
            ar = w/float(h)
            if ar>= 0.95 and ar<=1.05:
                shape = 'Square'
            else:
                shape = 'Rectangle'
        elif len(approx) == 5:
            shape='pentagon'
        elif len(approx) == 6:
            shape= 'Hexagon'
        else:
            shape = 'circle'

        cv2.drawContours(img, [c], -1, (0, 23, 23), 3)
        cv2.circle(img, (cX, cY), 2, (0, 0, 0), -1)
        cv2.putText(img,shape,(cX+4,cY+4),cv2.FONT_ITALIC,0.7,(23,34,56),2)




shape_detection(img,cnts)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()