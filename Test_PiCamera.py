from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.resolution = (2592, 1944)
camera.framerate = 15
#camera.start_preview()
sleep(5)
camera.capture('/home/pi/Documents/Img/ByPICamera/image4.jpg')
camera.stop_preview()