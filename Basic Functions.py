import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)

path=r"C:\Users\IT-Admin\Downloads\wp6809345.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(640,480))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.resize(gray,(640,480))
# blur=cv2.GaussianBlur(gray,(5,5),0)
imgCanny=cv2.Canny(gray,100,500)
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDilation,kernel,iterations=1)
cv2.imshow("Dilation",imgDilation)
cv2.imshow( "Canny",imgCanny)
cv2.imshow("Eroded",imgEroded)
# cv2.imshow("Orignal",gray)
cv2.waitKey(0)