import cv2
import numpy as np

# Load the image
image = cv2.imread('..\Shapes\DrawnTriangle.jpg')
# image = cv2.imread('Shapes\Irregular_Pentagon.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours to find the triangle
for contour in contours:
    # Approximate the contour to a polygon with fewer vertices
    epsilon = 0.04 * cv2.arcLength(contour, True)  # Change 0.04 based on the image quality
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # If the approximated contour has 3 vertices, it's a triangle
    if len(approx) >= 3:
        # Draw the triangle on the image
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        
        # Print the vertices of the triangle
        print("Vertices of the triangle:", approx)

        # Show the vertices on the image
        for point in approx:
            cv2.circle(image, tuple(point[0]), 5, (0, 0, 255), -1)

# Display the image with the triangle marked
cv2.imshow('Triangle Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# how to detect vertices of a triangle drawn on a paper when image of that page is clicked



'''
cap = cv2.VideoCapture(0)  # Open webcam

# Set scale factor based on reference object (e.g., 1 cm = 50 pixels)
cm_per_pixel = 0.02

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:
        break

    # Image processing and distance calculation code goes here (same as above)
    
    cv2.imshow('Polygon Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
