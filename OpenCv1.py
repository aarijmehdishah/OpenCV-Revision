import cv2
path=r"C:\Users\IT-Admin\Downloads\wp6809345.jpg"
img=cv2.imread(path)
img=cv2.resize(img,(640,480))
# img1=cv2.imread(path,0)#convert to grayscale
# img1=cv2.resize(img,(640,480))
# cv2.imshow( "Original",img)
# cv2.imshow( "GrayScale",img1)
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow( "GaussianBlur",blur)
# cv2.imshow("GrayScale",grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()git i