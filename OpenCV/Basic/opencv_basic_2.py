# Edge detection
import cv2
import immmm
import matplotlib.pyplot as plt

img = cv2.imread('tetris.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(img,70,150)
plt.title("Edge detection")
plt.imshow(edged)
plt.show()

# thresholding
print(img.shape)
_, thresh = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
plt.title('Thresholding')
plt.imshow(thresh)
plt.show()

# find Contours
cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = immmm.grab_contours(cnts)
output = img.copy()

for c in cnts:
    cv2.drawContours(output,[c],-1,(240,0,150),3)
    plt.imshow(output)
    plt.show()

text = f"I get {len(cnts)} objects"
cv2.putText(output,text,(60,60),cv2.FONT_ITALIC,0.8,(123,152,134),3)
plt.imshow(output)
plt.title('Counters')
plt.show()

# Erosions and Dilations are typically used to reduce noise in binary image
# A side effect of thresholding

# Masks allow us to mask out regions of an image we are uninterested in.
# We call them 'masks' because they will hide regions of images we do not care about.


