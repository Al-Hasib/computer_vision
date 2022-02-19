import cv2
import pyautogui as p
import numpy as np

size = p.size()

file = 'screen_record.avi'

video = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(file,video,25,size)

# create recording module
cv2.namedWindow('Recording..',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Resized window',780,600)

while True:
    img = p.screenshot()
    img = np.array(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("recording",img)
    output.write(img)
    if cv2.waitKey(25) & 0XFF==ord('q'):
        break
output.release()
cv2.destroyAllWindows()