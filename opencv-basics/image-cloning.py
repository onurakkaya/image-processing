import cv2
import numpy as np

image = cv2.imread("opencv-basics\image.jpg")

Blue = image[:,:,0]
Green = image[:,:,1]
Red = image[:,:,2]

# We're getting width , height and channel information from shape property of image object.
width, height, channels = image.shape

# We need to create empty array to fill the image pixels.
# We'll use width,height and channel information.
cloneImage = np.zeros([width,height,channels],np.uint8)

#We're loading layers of the empty array from the our original image.
cloneImage[:,:,0] = Blue
cloneImage[:,:,1] = Green
cloneImage[:,:,2] = Red

cv2.imshow("Original Image",image)
cv2.imshow("Clone Image",cloneImage)

cv2.waitKey(0)