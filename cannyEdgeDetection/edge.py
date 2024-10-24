import cv2
import numpy as np

#block to remove background from image

#block to add a plain white background to the image 

# Load and convert the image to grayscale
image = cv2.imread('test2.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform edge detection  can you add the code to first convert the image to grey scale 
gradients_sobelx = cv2.Sobel(image, -1, 1, 0)
gradients_sobely = cv2.Sobel(image, -1, 0, 1)
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

gradients_laplacian = cv2.Laplacian(image, -1)

canny_output = cv2.Canny(image, 80, 150)

# Set window size
# cv2.namedWindow('Sobel x', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Sobel x', 600, 600)

# cv2.namedWindow('Sobel y', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Sobel y', 600, 600)

# cv2.namedWindow('Sobel X+y', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Sobel X+y', 600, 600)

# cv2.namedWindow('laplacian', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('laplacian', 600, 600)

cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canny', 600, 600)

# Display the images
# cv2.imshow('Sobel x', gradients_sobelx)
# cv2.imshow('Sobel y', gradients_sobely)
# cv2.imshow('Sobel X+y', gradients_sobelxy)
# cv2.imshow('laplacian', gradients_laplacian)
cv2.imshow('Canny', canny_output)

cv2.waitKey(0)
cv2.destroyAllWindows()

