This folder contains the source code for the Gunshot Detection System project. It includes the code for the various components of the system, such as the ESP32-based microphone nodes, Raspberry Pi for source localization, and the machine learning model.

Table of Contents

    Folder Structure

    ESP32 Code

    Raspberry Pi Code

    Machine Learning Code

    Dependencies

    Building and Running

Folder Structure

The src/ folder is organized into the following subfolders:

    esp32/: Contains the code for the ESP32-based microphone nodes.

    raspberry-pi/: Contains the code for the Raspberry Pi, which handles source localization and TDoA calculations.

    machine-learning/: Contains the code for training and deploying the machine learning model for gunshot detection.

ESP32 Code 

This folder contains the source code for the ESP32 devices used to capture audio from microphones, detect gunshots, and send data for further processing.
Key Files:

    main.cpp: The main entry point for the ESP32 application, handling microphone input, audio processing, and communication.

Building and Flashing:

    Use the Arduino IDE to upload the code to the ESP32.

    Make sure to select the appropriate board and port before flashing.

Raspberry Pi Code 

This folder contains the code for the Raspberry Pi, which is responsible for the time-difference-of-arrival (TDoA) algorithm to localize gunshots.
Key Files:

    main.py: The main entry point for the Raspberry Pi application, which calculates the TDoA based on microphone inputs.

    localization.py: The algorithm for calculating the source location based on TDoA values.

    config.json: Configuration file for setting the parameters of the localization algorithm.

Running the Code:

    The code can be run by executing the following command:

    python3 main.py

Machine Learning Code

This folder contains the code for training and deploying the machine learning model to detect gunshots based on audio data.
Key Files:

    train_model.py: Script for training the machine learning model on audio data.

    predict.py: Script for running the model inference on new audio data.

    model/: Contains the saved models used for detection.

Requirements:

    Install required Python dependencies:

    pip install -r requirements.txt

Running the Training Script:

    To train the model, run the following command:

    python3 train_model.py

Dependencies

The following dependencies are required to build and run the code:
ESP32 Code:

    Arduino IDE

    ESP32 Arduino core

Raspberry Pi Code:

    Python 3.x

    numpy

    scipy

    matplotlib

Machine Learning Code:

    Python 3.x

    tensorflow 
    
    librosa 
    
    numpy 

    matplotlib 

    scikit-learn


Building and Running
ESP32:

    Open the ESP32 code in Arduino IDE.

    Select the correct board and port.

    Upload the code to the ESP32.

Raspberry Pi:

    Install Python dependencies on the Raspberry Pi.

    Run the main script:

    python3 main.py

Machine Learning Model:

    Train the model using the train_model.py script.

    Run inference on audio samples using the predict.py script.
