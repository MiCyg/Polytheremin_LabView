# Description
This application provides integration and testing of acquisition and processing techniques, as well as data collection for the development of a decorrelation algorithm.  
It uses my previously built PolyTheremin [testing platform](https://github.com/MiCyg/PolyTheremin_Hardware) to detect hand gestures and measure distances between fingers and the proximity sensors.  
For detect a hand movement, the application uses [mediapipe](https://github.com/google-ai-edge/mediapipe) library. In this case, you should have the proper Python version and the necessary library installed, but don't worry. I have created an installer for this.

# Before opening LabView...
Run the [installation script](pythonInstallation.bat), which will install the proper Python version and create a virtual environment for the mediapipe library.

# Hardware
- My PolyTheremin [testing platform](https://github.com/MiCyg/PolyTheremin_Hardware)
- Camera
- cDAQ-9171 USB chassis
- NI9215 module

# Application Presentation
Example usage and all implemented functions was presented on video.



# Contribution
If you find any issues, feel free to open a pull request and describe the problem. 


