import cv2

#This function is used to read an image from the file to array with the Opencv
image = cv2.imread("opencv-basics\image.jpg")


#This function is used to show image array to the screen. 
#First parameter is title of the screen.
#Second parameter is an image array
cv2.imshow("Origin",image)

#The waitKey function prevents to close screens after drawed to screen (blink)
cv2.waitKey(0)