import cv2
import matplotlib.pyplot as plt

image = cv2.imread('me.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

print(image.shape)

roi = image[330:700,645:940]
plt.imshow(image)
plt.imshow(roi)
plt.show()
cv2.imwrite('roi.png',roi)