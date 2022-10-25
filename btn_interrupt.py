import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def handler(channel):
    print("Clicked")

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24, GPIO.RISING, callback=handler, bouncetime=300)
while True:
    time.sleep(1)