import cv2
#import imutils

# read the images
img = cv2.imread('nature.jpg')
img1 = cv2.imread('nature_1.jpg')
img2 = cv2.imread('nature_2.jpg')

arr = [[img],[img1,img2]]

add = []