import cv2
import imutils
import glob

imageList = [cv2.imread(img) for img in glob.glob('../Basic/make_gif/*.jpg')]
print(len(imageList))
'''
# read the images
img = cv2.imread('../Project/stackImage/nature.jpg')
shape = img.shape
print(f'Height : {shape[0]},width: {shape[1]},channel: {shape[2]}')

# resize the images by width and height
width = 700
height = 400
img_1 = cv2.resize(img,(width,height))

# resize image by scale factor of X-axis and Y-axis
img_2 = cv2.resize(img,(0,0),None,1.2,1.2,interpolation=cv2.INTER_CUBIC)

# resize the image by only giving the width or height by imutils
img_3 = imutils.resize(img,width=700,height=None,inter=cv2.INTER_CUBIC)

cv2.imshow('img',img)
cv2.imshow('img_1',img_1)
cv2.imshow('img_2',img_2)
cv2.imshow('img_3',img_3)


cv2.waitKey(0)
cv2.destroyAllWindows()
'''
def resize_img(imgList,width=400,height=300):
    resized_img = [cv2.resize(img,(width,height)) for img in imgList]
    for index,i in enumerate(resized_img):
        cv2.imwrite(f'../Basic/make_gif/{index}.jpg',i)


resize_img(imageList)


