import cv2

image = cv2.imread("opencv-basics\image.jpg")

# image [ first, second, third]
#  -> first parameter is used to select coord of x-axis (":" means select all pixels )
#  -> second parameter is used to select coord of y-axis
#  -> third paramter is used to select the color layer.
#      ->> The layer order is;
#      --> In order of; Blue, Green and Red for non transparent images like a jpeg
#      --> In order of; Blue, Green, Red and Alpha for transparency supported images like a png. ( Alpha is the opacity layer.)

# Pixels selected in the Blue Layer (B)
BlueLayer = image[:,:,0]  

# Pixels selected in the Green Layer (G)
GreenLayer = image[:,:,1]  

# Pixels selected in the Red Layer (R)
RedLayer = image[:,:,2] 

cv2.imshow("Origin",image)

cv2.imshow("Only Red",RedLayer)
cv2.imshow("Only Green",GreenLayer)
cv2.imshow("Only Blue",BlueLayer)

cv2.waitKey(0)