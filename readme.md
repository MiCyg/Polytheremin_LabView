
# Description

More details are available in the [PolyTheremin repository](https://github.com/MiCyg/PolyTheremin) which is in development now.  

This application integrates and tests acquisition and processing techniques while collecting data to support the development of a decorrelation algorithm. It uses the [PolyTheremin testing platform](https://github.com/MiCyg/PolyTheremin_Hardware) to detect hand gestures and measure distances between fingers and proximity sensors.  

Hand movement detection is achieved using the [Mediapipe library](https://github.com/google-ai-edge/mediapipe). To simplify setup, an installer has been created to install the required Python version and dependencies.

# Before Launching LabVIEW
Run the [installation script](pythonInstallation.bat) to set up the correct Python version, create a virtual environment, and install the Mediapipe library.  

[PolyTheremin Installation](https://github.com/user-attachments/assets/24161088-da3a-4458-9bec-f73b979741b2)

If the script does not work, you can either contact me for help or manually install the dependencies:  
1. Install **Python 3.10.0**
2. Create a virtual environment named `mp_env` in the `vision/python/` folder
3. Install the Mediapipe library in the `mp_env` environment


# Hardware Requirements  
- [PolyTheremin testing platform](https://github.com/MiCyg/PolyTheremin_Hardware)  
- Camera  
- cDAQ-9171 USB chassis  
- NI9215 module  

# Application Demo  
Watch the video below for an example of the application and its features:  

[![PolyTheremin Presentation](https://img.youtube.com/vi/Dlh9XJ3kCwI/0.jpg)](https://www.youtube.com/watch?v=Dlh9XJ3kCwI)  

# Application window description

## Setup
- Proximitor parameters - Set the cDAQ channels, sample rate and buffer size. Default values should be suspicious so i would recommend to change them.
- Output sound format - Set your output card for audio generation
- Proximitor scalling - Each proximitor can be independly scaled fitted to your hardware and heterodyne generator
- Scalling offset - Add offset to proximitor measurement
 
## Dac
Shows a measurement graph, just for test.

## Vision
- Camera source - For select camera input
- Test button - Test video from camera
- Antenna sellector - can you choose antenna positions by mouse clicking the video pane
- Reverse fingers - match hand direction
- Ant Distance - Collating real distance [mm] and mean video distance [px] for calculate real distances between fingers and antennas    
- FPS - Shows FPS

## Correlation
Shows Correlation plot, just for test

## File Saver
- File Save button - Start and stop data aquisition to file
- File path - Choose your tdms file path 



# Contributions  
If you encounter any issues, feel free to open a pull request and describe the problem.
