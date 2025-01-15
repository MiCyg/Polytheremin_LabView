@echo off

set "PYTHON_STUFF_DIR=%~dp0vision\python"
set "INSTALLATION_DIR=%PYTHON_STUFF_DIR%\installation"

:: Specify the version of Python we want to download
set "PYTHON_VERSION_SHORT=3.10"
set "PYTHON_VERSION=%PYTHON_VERSION_SHORT%.0"

set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
set "EXE_NAME=python-%PYTHON_VERSION%-amd64.exe"
set "VIRTUAL_ENV_NAME=mp_env"

:: Check if the system is 64-bit
if NOT "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    echo Cannot run this application on 32-bit OS. Sorry.
    pause
    exit /b 1
)

:: Create installation directory if it doesn't exist
if not exist "%INSTALLATION_DIR%" mkdir "%INSTALLATION_DIR%"

:: Download Python installer if the file doesn't exist
if not exist "%INSTALLATION_DIR%\%EXE_NAME%" (
    echo Downloading Python %PYTHON_VERSION%.
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %INSTALLATION_DIR%\%EXE_NAME%"
)

:: Check if the installer has been downloaded
if not exist "%INSTALLATION_DIR%\%EXE_NAME%" (
    echo Error downloading file. Check your internet connection.
    pause
    exit /b 1
)

:: Run the .exe installer
echo Starting Python installation.
"%INSTALLATION_DIR%\%EXE_NAME%"

:: Check if the installation was successful
if %errorlevel% neq 0 (
    echo Error during installation. Check your installation file.
    pause
    exit /b 1
)

:: Confirmation of successful installation
echo Python %PYTHON_VERSION% has been installed successfully!

:: Create virtual environment for the application
echo Creating virtual environment for application.
py -%PYTHON_VERSION_SHORT% -m venv %PYTHON_STUFF_DIR%\%VIRTUAL_ENV_NAME%
:: Check if virtual environment was created successfully
if not exist "%PYTHON_STUFF_DIR%\%VIRTUAL_ENV_NAME%\Scripts\python.exe" (
    echo Virtual environment creation failed.
    pause
    exit /b 1
)

:: Install mediapipe
echo Installing mediapipe.
"%PYTHON_STUFF_DIR%\%VIRTUAL_ENV_NAME%\Scripts\python.exe" -m pip install mediapipe

:: Clean up the installer and installation directory
echo Cleaning up.
del "%INSTALLATION_DIR%\%EXE_NAME%"
rmdir /s /q "%INSTALLATION_DIR%"

echo Virtual environment for PolyTheremin is ready to use!
echo Happy Theremining :)
pause