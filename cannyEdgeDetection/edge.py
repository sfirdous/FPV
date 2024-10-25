import cv2
import numpy as np

# Load the image
image = cv2.imread('testx.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Block to remove the background
# Apply a binary threshold to separate the foreground from the background
_, thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours from the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask to remove the background
mask = np.zeros_like(gray_image)
cv2.drawContours(mask, contours, -1, (255), thickness=cv2.FILLED)

# Apply the mask to the original image to remove the background
foreground = cv2.bitwise_and(image, image, mask=mask)

# Display the image after background removal
cv2.namedWindow('After Background Removal', cv2.WINDOW_NORMAL)
cv2.resizeWindow('After Background Removal', 600, 600)
cv2.imshow('After Background Removal', foreground)

# Block to add a plain white background to the image
# Create a white background image of the same size
background = np.ones_like(image, dtype=np.uint8) * 255
background = cv2.bitwise_and(background, background, mask=cv2.bitwise_not(mask))
final_image = cv2.add(foreground, background)

# Display the image after adding a white background
cv2.namedWindow('With White Background', cv2.WINDOW_NORMAL)
cv2.resizeWindow('With White Background', 600, 600)
cv2.imshow('With White Background', final_image)

# Convert the image with white background to grayscale for edge detection
gray_final_image = cv2.cvtColor(final_image, cv2.COLOR_BGR2GRAY)

# Perform edge detection using Sobel operators
gradients_sobelx = cv2.Sobel(gray_final_image, cv2.CV_64F, 1, 0)
gradients_sobely = cv2.Sobel(gray_final_image, cv2.CV_64F, 0, 1)
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

# Perform edge detection using Laplacian operator
gradients_laplacian = cv2.Laplacian(gray_final_image, cv2.CV_64F)

# Perform edge detection using Canny
canny_output = cv2.Canny(gray_final_image, 80, 150)

# Display the Canny edge detection result
cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canny', 600, 600)
cv2.imshow('Canny', canny_output)

cv2.waitKey(0)
cv2.destroyAllWindows()


