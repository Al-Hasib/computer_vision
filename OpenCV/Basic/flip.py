import cv2

img = cv2.imread('roi.png')

flip_0 = cv2.flip(img,0)
flip_1 = cv2.flip(img,1)
flip__1 = cv2.flip(img,-1)

cv2.imshow('Original',img)
cv2.imshow('flip_x-axis',flip_0)
cv2.imshow('flip_y-axis',flip_1)
cv2.imshow('flip_both-axis',flip__1)


cv2.waitKey(0)
cv2.destroyAllWindows()