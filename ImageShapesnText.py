import cv2
import numpy as np

img= np.zeros((512,512,3),np.uint8)

#img[256:271]=(255,0,0)
cv2.line(img,(0,0),(512,512),(255,0,255),2)
cv2.rectangle(img,(300,50),(410,150),(0,0,255),cv2.FILLED)
cv2.circle(img,(50,450),35,(255,255,255),5)
cv2.putText(img,"Welcome Back to CV2",(100,30),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2)

cv2.imshow("Image",img)
cv2.waitKey(0)
