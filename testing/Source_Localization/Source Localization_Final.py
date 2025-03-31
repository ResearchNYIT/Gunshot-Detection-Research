import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

#  Step 1: Simulate TDoA 
def simulate_tdoa(mic_positions, source_position, speed_of_sound):
    """
    Simulate TDoA values given microphone positions and the true source position.
    """
    distances = np.linalg.norm(mic_positions - source_position, axis=1)
    arrival_times = distances / speed_of_sound
    tdoa = arrival_times - arrival_times[0]  # Relative to the first mic
    return tdoa

#  Step 2: Source Localization (Nonlinear Least Squares) 
def TDoA_Least_Squares(mic_positions, tdoa, speed_of_sound):
    """
    Estimate the source position using nonlinear least squares to minimize TDoA error.
    """
    def tdoa_error(estimated_position):
        # Compute predicted distances and TDoAs in 3D
        distances = np.linalg.norm(mic_positions - estimated_position, axis=1)
        predicted_tdoa = (distances - distances[0]) / speed_of_sound
        return tdoa - predicted_tdoa

    # Initial guess: center of the microphone array
    initial_guess = np.mean(mic_positions, axis=0)

    # Perform least squares 
    result = least_squares(tdoa_error, initial_guess)

    return result.x  # Optimized position

#  Step 3: Calculate Camera Direction (3D) 
def calculate_camera_direction(source_position, camera_position):
    """
    Calculate the 3D direction for the camera to face the sound source.
    """
    direction_vector = source_position - camera_position
    norm = np.linalg.norm(direction_vector)
    direction_unit = direction_vector / norm  # Normalize the vector to get direction

    # Calculate XY and elevation angles
    XY = np.degrees(np.arctan2(direction_unit[1], direction_unit[0]))  # XY plane
    elevation = np.degrees(np.arcsin(direction_unit[2]))  # Z direction

    return direction_unit, XY, elevation

#  Step 4: Visualization (3D Plot) 
def plot_system(mic_positions, true_source, estimated_position, camera_position, camera_direction, camera_angle):
    """
    Plot the system in 3D with positions of microphones, true sound source,
    estimated position, and camera direction.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot microphones, true source, and estimated position
    ax.scatter(mic_positions[:, 0], mic_positions[:, 1], mic_positions[:, 2], c='blue', label='Microphones')
    ax.scatter(*true_source, c='red', label='True Sound Source')
    ax.scatter(*estimated_position, c='green', label='Estimated Sound Source')
    ax.scatter(*camera_position, c='purple', label='Camera')

    # Plot the camera direction in 3D using a quiver plot
    ax.quiver(camera_position[0], camera_position[1], camera_position[2],
              camera_direction[0], camera_direction[1], camera_direction[2],
              color='purple', length=0.3, label='Camera Direction')

    # Set axis limits and labels
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_zlim(-0.5, 1.5)
    ax.set_xlabel("X Position (m)")
    ax.set_ylabel("Y Position (m)")
    ax.set_zlabel("Z Position (m)")
    ax.grid()
    ax.legend()
    ax.set_title("3D Source Localization System")

    plt.show()

#  Main Execution 

# Microphone positions (in meters) now in 3D
mic_positions = np.array([
    [0, 0, 0],  # Bottom-left corner
    [1, 0, 0],  # Bottom-right corner
    [0, 1, 0],  # Top-left corner
    [1, 1, 0]   # Top-right corner
])

# True sound source position (in 3D, for simulation/testing only)
true_source = np.array([1.25, 1.0, 0.5])  # True position (unknown in real use)

# Speed of sound (in meters per second)
speed_of_sound = 343

# Simulate TDoA values
observed_tdoa = simulate_tdoa(mic_positions, true_source, speed_of_sound)

# Perform localization
estimated_position =  TDoA_Least_Squares(mic_positions, observed_tdoa, speed_of_sound)

# Set camera position 
camera_position = [1,1,1]

# Calculate the camera's 3D direction vector and angles
camera_direction, camera_angle_XY, camera_angle_elevation = calculate_camera_direction(estimated_position, camera_position)

# Print Results
print(f"True Sound Source Position: {true_source}")
print(f"Estimated Source Position: {estimated_position}")
print(f"Camera XY Angle (degrees): {camera_angle_XY}")
print(f"Camera Elevation Angle (degrees): {camera_angle_elevation}")

# Visualize the system in 3D
plot_system(mic_positions, true_source, estimated_position, camera_position, camera_direction, camera_angle_XY)
