import argparse
import imutils
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument('-i','--input',required=True,
                help = 'path of the image')
ap.add_argument('-o','--output',required=True,
                help = 'path of the output_image')

args = vars(ap.parse_args())

image = cv.imread(args['input'])

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray,(5,5),0)
thresh = cv.threshold(blurred,70,255,cv.THRESH_BINARY)[1]


cv.imwrite(args['output'],gray)
cv.imwrite(args['output'],blurred)
cv.imwrite(args['output'],thresh)