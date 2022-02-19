from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2
import argparse
import imutils


class ColorLabeler:
    def __init__(self):
        colors = OrderedDict({
            'red': (255,0,0),
            'green':(0,255,0),
            'blue':(0,0,255)
        })
        self.lab = np.zeros((len(colors),1,3),dtype='uint8')
        self.colorNames = []

        for (i,(name,rgb)) in enumerate(colors.items()):
            self.lab[i] = rgb
            self.colorNames.append(name)

        self.lab = cv2.cvtColor(self.lab,cv2.COLOR_BGR2LAB)

    def label(self,image,c):
        mask = np.zeros(image.shape[:2],dtype='uint8')
        cv2.drawContours(mask,[c],-1,255,-1)
        mask = cv2.erode(mask,None,iterations=2)
        mean= cv2.mean(image,mask=mask)[:3]

        minDist = (np.inf,None)

        for (i,row) in enumerate(self.lab):
            d = dist.euclidean(row[0],mean)

            if d<minDist[0]:
                minDist = (d,i)
        return self.colorNames[minDist[1]]

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help = 'path of the input image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
resized = imutils.resize(image,width=400)

blurred = cv2.GaussianBlur(resized,(5,5),0)
gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred,cv2.COLOR_BGR2LAB)
thresh = cv2.threshold(gray,190,255,cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

def shape_detection(c):
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
    return shape

cl = ColorLabeler()

for c in cnts:
    M = cv2.moments(c)
    if M['m00'] == 0:
        M['m00'] = 0.001
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])

    shape = shape_detection(c)
    color = cl.label(lab,c)

    text = f"{color} {shape}"
    cv2.drawContours(image,[c],-1,(0,255,0,2))
    cv2.putText(image,text,(cX,cY),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,23),2)
    cv2.imshow("image",image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
