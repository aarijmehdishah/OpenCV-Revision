import cv2

frameWidth = 920
frameHeight = 1080

video=cv2.VideoCapture(r"C:\Users\IT-Admin\Downloads\istockphoto-1455749437-640_adpp_is.mp4")

while True:
    success,img=video.read()
    img=cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("Original",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break