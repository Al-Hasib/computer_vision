# import the library
import cv2
#import imutils

# read the images
img = cv2.imread('nature.jpg')
img1 = cv2.imread('nature_1.jpg')
img2 = cv2.imread('nature_2.jpg')
img3 = cv2.imread('nature_3.jpg')
img4 = cv2.imread('nature_4.jpg')

def resize(img):
    img = cv2.resize(img,(300,250))
    return img

def hstack(imgList):
    imgList = [resize(img) for img in imgList]
    return cv2.hconcat(imgList)

def vstack(imgList):
    imgList = [resize(img) for img in imgList]
    return cv2.vconcat(imgList)

def hstack_vstack(imgList):
    add = []
    for i in imgList:
        img_vstack = vstack()
        cv2.imshow('img_vstack',img_vstack)





hstack = hstack([img,img1,img2,img3])
vstack = vstack([img,img1])
hstack_vstack = hstack_vstack([[img,img1],[img2],[img3,img4]])

cv2.imshow('Horigental Stack',hstack)
cv2.imshow('Vertically stack',vstack)
#cv2.imshow('hstack_vstack',hstack_vstack)


cv2.waitKey(0)
cv2.destroyAllWindows()