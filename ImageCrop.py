import cv2

path=r"Resources/lenna.png"
img=cv2.imread(path)
print(img.shape)
width=100
height=100
imgresized=cv2.resize(img,(width,height))
imgCrop=img[250:290,250:400]
print(imgCrop.shape)
imgCropResize=cv2.resize(imgCrop,(img.shape[1],img.shape[0]))
cv2.imshow("Resized Crop",imgCropResize)
cv2.imshow("Lena",img)
#cv2.imshow("Lena Resized",imgresized)
cv2.imshow("Lena Cropped",imgCrop)
cv2.waitKey(0)