import cv2
import numpy as np

# Load the image
image = cv2.imread('..\Shapes\DrawnTriangle2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Measure a reference object (e.g., a ruler)
# For example, if you know that 1cm = 50 pixels in the image, set a known length in centimeters
cm_per_pixel = 0.02  # For instance, 1 cm = 50 pixels, then cm_per_pixel = 1/50 = 0.02 cm/pixel

# Iterate through contours to find the polygon
for contour in contours:
    # Approximate the contour to a polygon with fewer vertices
    epsilon = 0.04 * cv2.arcLength(contour, True)  # Adjust epsilon based on the image quality
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # If the approximated contour has exactly 3 vertices, it's a triangle
    if len(approx) == 3:
        # Draw the polygon on the image
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

        # Print the vertices of the triangle
        print("Vertices of the triangle:", approx)

        # Calculate and display the length between consecutive vertices
        for i in range(len(approx)):
            # Get the coordinates of the current and next point
            pt1 = approx[i][0]
            pt2 = approx[(i + 1) % len(approx)][0]  # (i + 1) % len(approx) wraps around to the first point

            # Calculate Euclidean distance (distance between pt1 and pt2) in pixels
            distance_pixels = np.linalg.norm(pt2 - pt1)

            # Convert the distance to centimeters using the scale (cm_per_pixel)
            distance_cm = distance_pixels * cm_per_pixel

            print(f"Distance between {tuple(pt1)} and {tuple(pt2)}: {distance_cm:.2f} cm")

            # Display the distance on the image
            mid_point = ((pt1[0] + pt2[0]) // 2, (pt1[1] + pt2[1]) // 2)  # Midpoint to place the text
            cv2.putText(image, f"{distance_cm:.2f} cm", mid_point, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

            # Optionally, draw a line connecting the points
            cv2.line(image, tuple(pt1), tuple(pt2), (255, 0, 0), 2)

        # Show the vertices on the image
        for point in approx:
            cv2.circle(image, tuple(point[0]), 5, (0, 0, 255), -1)

# Display the image with the polygon and distances
cv2.imshow('Triangle Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
