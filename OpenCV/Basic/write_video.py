import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('my_video.avi',fourcc,20,(640,480)) # 0 for gray Scale

while cap.isOpened():
    ret,frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        lab = cv2.cvtColor(frame,cv2.COLOR_BGR2LAB)
        cv2.imshow('video',frame)
        cv2.imshow('video_lab',lab)
        cv2.imshow('video_gray',gray)
        output.write(frame)
        if cv2.waitKey(25) & 0XFF == ord('q'):
            break
cap.release()
output.release()
cv2.destroyAllWindows()