
3D Sound Source Localization and Camera Orientation Script

This Python script demonstrates the localization of a sound source in 3D space using Time Difference of Arrival (TDoA) and orients a camera to face the sound source. 
It also includes a visualization of the setup.

---

 Features

1. TDoA Simulation:
   - Simulates Time Difference of Arrival values for a sound source given known microphone positions.

2. Source Localization:
   - Uses nonlinear least squares optimization to estimate the 3D position of the sound source.

3. Camera Orientation:
   - Calculates the direction and angles (azimuth and elevation) for the camera to point towards the sound source.

4. 3D Visualization:
   - Displays the positions of microphones, the true and estimated sound source positions, and the camera setup in a 3D plot.

---

 Requirements

 Installing Python

1. Download Python from the [official website](https://www.python.org/downloads/).
2. Follow the installation instructions for your operating system:
   - On Windows, ensure you check the box to "Add Python to PATH" during installation.
   - On macOS and Linux, Python is often pre-installed. 

3. Verify the installation:

   python --version  


 Python Libraries

The script uses the following Python libraries:
- `numpy`: For numerical operations.
- `matplotlib`: For 3D visualizations.
- `scipy`: For least squares optimization.

Install the dependencies using pip:

pip install numpy matplotlib scipy


---

 How It Works

1. Simulate TDoA:
   - Computes the Time Difference of Arrival (TDoA) values for microphones based on their distances from the sound source.

2. Source Localization:
   - Estimates the 3D source position by minimizing the error between observed and predicted TDoA values.

3. Camera Orientation:
   - Computes the direction vector for the camera to face the sound source and calculates XY and elevation angles.

4. Visualization:
   - Plots:
     - Microphone positions
     - True and estimated sound source positions
     - Camera position and direction

---

 Usage

1. Save the Script:
   - Save the provided Python code as a file, e.g., `tdoa_source_localization.py`.

2. Run the Script:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script and run:
     python tdoa_source_localization.py 
Or
     python3 tdoa_source_localization.py on some systems


3. View Outputs:
   - The true and estimated sound source positions and camera angles will be printed.
   - A 3D plot will visualize the setup.

---

 Customization

1. Modify Microphone Array:
   - Update the `mic_positions` array to reflect the physical arrangement of your microphone array.

2. Set True Source Position:
   - Change `true_source` to test different source positions.

3. Adjust Speed of Sound:
   - Modify `speed_of_sound` to adapt to different environments (e.g., air, water).

4. Change Camera Position:
   - Update `camera_position` to specify the starting location of the camera.

---
 Notes

- This script is a simulation. In real-world applications, TDoA values would come from actual microphone recordings.
---
 
