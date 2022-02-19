import cv2
import matplotlib.pyplot as plt
import imutils

img = cv2.imread('me.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

resize_1 = cv2.resize(img,(300,300))
cv2.imwrite('resized_1.png',resize_1)

(h,w,d) = img.shape
r = 300.0/w
dim = (300,int(h*r))
resize_2 = cv2.resize(img,dim)
cv2.imwrite('resize_2.png',resize_2)

# use imutils easily

resize_imutils = imutils.resize(img,width=300)
#plt.imshow(resize_imutils)
plt.show()
cv2.imwrite('resize_imutils.png',resize_imutils)


# Rotate Image
center = (w//2,h//2)
M = cv2.getRotationMatrix2D(center,-45,1.0)
rotated = cv2.warpAffine(img,M,(w,h))
''' plt.imshow(rotated)
plt.show()
'''
cv2.imwrite('rotated.png',rotated)

rotated_imutils = imutils.rotate(img,-45)
''' plt.title('RoTated image using imultils')
plt.imshow(rotated_imutils)
plt.show()
'''

roated_bound = imutils.rotate_bound(img,45)
cv2.imwrite('roated_bound.png',roated_bound)

G_blur = cv2.GaussianBlur(img,(7,7),0)
plt.title('Baussian Blur')
plt.imshow(G_blur)
plt.show()
cv2.imwrite('Gaussian_blur.png',G_blur)

#Draw rectangle on image
rect = img.copy()
cv2.rectangle(rect,(700,300),(950,700),(123,223,34),6)
plt.title('Rectangle on image')
plt.imshow(rect)
plt.show()
cv2.imwrite('Rectangle_image.png',rect)

circle = img.copy()
# use -1 thickness for filled the circle
cv2.circle(circle,(800,500),130,(123,223,34),6)
plt.title('Circle on image')
plt.imshow(circle)
plt.show()
cv2.imwrite('Circle_image.png',circle)

#draw text in image
text = img.copy()
cv2.putText(text,"Abdullah",(800,500),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,34,23),5)
plt.imshow(text)
plt.show()
cv2.imwrite('Put text on image.png',text)