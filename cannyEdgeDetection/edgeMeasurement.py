import cv2
import numpy as np

# Load the image
image = cv2.imread('test.jpg')

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

# Perform edge detection using Canny
canny_output = cv2.Canny(gray_final_image, 80, 150)

# Display the Canny edge detection result
cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canny', 600, 600)
cv2.imshow('Canny', canny_output)

# New Block: Find contours from the Canny output and calculate dimensions
# Find contours from the Canny output
canny_contours, _ = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over each contour and measure dimensions
for i, contour in enumerate(canny_contours):
    # Calculate bounding box dimensions for each contour
    x, y, w, h = cv2.boundingRect(contour)
    length = cv2.arcLength(contour, True)  # Approximate length of the edge
    area = cv2.contourArea(contour)        # Area of the contour, if needed

    # Draw the bounding box and display the dimensions
    cv2.rectangle(final_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(final_image, f"L:{int(length)} W:{w} H:{h}", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# Display the final image with dimensions overlay
cv2.namedWindow('Dimensions on Detected Edges', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Dimensions on Detected Edges', 600, 600)
cv2.imshow('Dimensions on Detected Edges', final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
