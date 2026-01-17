# rpi4-camera-setup
A simple guide to test the Raspberry Pi camera in 2024+.
I created this because most tutorials on the internet are no longer valid: the old camera stack is gone, the raspi-config option disappeared, and Picamera2 is now the correct way to use CSI cameras. This repo shows the minimal steps that actually work today.

## 1) Update the system

Before doing anything with the camera, make sure the Raspberry Pi OS is fully updated.

Open a terminal and run:

```bash
sudo apt update
sudo apt full-upgrade -y
```

## 2) Install required system packages

On Raspberry Pi OS Bookworm the camera stack is already based on **libcamera**,  
so no legacy tools like `raspistill` are needed or even available.

What we need to install is the Python layer and tools that work with it.

Run this :
```bash
sudo apt install -y python3-picamera2
```
To check if the camera is working correctly run this :
```bash
rpicam-hello # this opens camera for 5 seconds
```
## 3) Create a Python virtual environment

Using a virtual environment keeps project dependencies separate from the system Python.  
This is especially useful on Raspberry Pi because Picamera2 is installed at system level while OpenCV will be installed with pip.

### Install venv support

```bash
cd ~
sudo apt install -y python3-venv
```
Create the environment
```bash
python3 -m venv venv --system-site-packages
```
The option --system-site-packages allows the virtual environment to access
the system-installed Picamera2 package while keeping other libraries isolated.

### Activate the environment
```bash
source venv/bin/activate
```

### Install OpenCV inside the environment
```bash
pip3 install --upgrade pip
pip3 install opencv-python
```

### Now you can run the python program 
```bash
python3 camera_test.py
```
press q to quit and deactivate the venv :
```bash
deactivate
```
