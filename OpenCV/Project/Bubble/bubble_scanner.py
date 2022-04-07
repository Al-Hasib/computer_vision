import cv2
import utils
import imutils

img1 = cv2.imread('images_1.jpg')
img = imutils.resize(img1,width= 400)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray_img,(3,3),0)
Edges = cv2.Canny(blur,50,70)

image_list = [img,gray_img,blur,Edges]
# build Montage only works with colorful Channels
# stack_image = imutils.build_montages(image_list,(128, 196),(5,5))

cv2.imshow('Original',img)
cv2.imshow('gray_img',gray_img)
cv2.imshow('blur',blur)
cv2.imshow('Edges',Edges)

cv2.waitKey(0)
cv2.destroyAllWindows()