import cv2

img = cv2.imread('me.jpg')


cv2.namedWindow('Thresh_trackbar')
def nothing(x):
    pass

cv2.createTrackbar("THRESH_VALUE",'Thresh_trackbar',0,255,nothing)

while True:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
    x = cv2.getTrackbarPos('THRESH_VALUE','Thresh_trackbar')
    Thresh_1 = cv2.threshold(gray_blur,x,255,cv2.THRESH_BINARY & cv2.THRESH_OTSU)[1]
    adaptive_thresh = cv2.adaptiveThreshold(gray_blur,255,
                                            cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY,11,2)
    res = cv2.bitwise_and(img,img,mask = Thresh_1)
    res_adaptive = cv2.bitwise_and(img,img,mask = adaptive_thresh)

    #cv2.imshow('org', img)
    #cv2.imshow('gray', gray)
    cv2.imshow('Thresh', Thresh_1)
    cv2.imshow('res_adaptive', adaptive_thresh)
    cv2.imshow('result', res)
    if cv2.waitKey(0) & 0XFF == ord('q'):
        break


cv2.destroyAllWindows()