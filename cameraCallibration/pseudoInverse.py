import numpy as np

# Define the intrinsic matrix P
# This matrix contains the camera's focal lengths (fx, fy) and the principal point coordinates (cx, cy).
fx, fy = 933.2709066392878, 924.716502790399
cx, cy = 495.05701189803943, 657.6301853051167
P = np.array([[fx, 0, cx],
              [0, fy, cy],
              [0,  0,  1]])

# Image points (2D) in homogeneous coordinates
# These are pixel coordinates from the image, with a third coordinate (1) added to make them homogeneous.
image_points = np.array([
    [113.03641, 375.4064 ,1],
[117.5, 381.5,1],
[847.7914  ,386.50024,1],
[924.54584 ,387.9133 ,1],
[1004.0971  , 386.04327,1],
[1008.8947 ,1260.1754,1],
[ 140.55122 ,1262.608 ,1 ],
[ 131.01913, 1265.9052,1 ],
])

# Compute the pseudoinverse of P
# The pseudoinverse is used to map image points back to the camera coordinate system approximately.
P_pseudo = np.linalg.pinv(P)

# Solve for 3D camera coordinates for each image point
# Multiply each image point by the pseudoinverse of P to find its corresponding 3D coordinates.
camera_coordinates = [P_pseudo @ point for point in image_points]

# Print the 3D camera coordinates
# Display the computed 3D coordinates for each image point.
for i, coord in enumerate(camera_coordinates, 1):
    print(f"3D Camera Coordinates for Point {i}: {coord}")

