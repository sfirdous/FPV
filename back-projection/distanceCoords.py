import numpy as np

# Example 3D camera coordinates
camera_coordinates = [
[-0.40933517 ,-0.30520033 , 1.        ]
,[-0.40455243 ,-0.29861064 , 1.        ]
 ,[ 0.37795498 ,-0.29320332  ,1.        ]
 ,[ 0.46019738 ,-0.29167522 , 1.        ]
 ,[ 0.54543658, -0.29369749  ,1.        ]
 ,[0.55057721, 0.65159994 ,1.        ]
,[-0.37985304  ,0.65423058  ,1.        ]
 ,[-0.39006668 , 0.65779621 , 1.        ]
]

# Convert to NumPy array for easier computation
camera_coordinates = np.array(camera_coordinates)

# Function to calculate Euclidean distance
def calculate_distance(point1, point2):
    return np.linalg.norm(point2 - point1)

# Calculate pairwise distances
for i in range(len(camera_coordinates)):
    for j in range(i + 1, len(camera_coordinates)):
        dist = calculate_distance(camera_coordinates[i], camera_coordinates[j])
        print(f"Distance between Point {i + 1} and Point {j + 1}: {dist:.4f}")
