!#/usr/bin/env python

import RPi.GPIO as GPIO
form mfrc522 import SimpleMFRC522

reader = SimpleMFRC522

try:
  text = input("New Data: ")
  print("Now place your tag to write")
  reader.write(text)
  print("Written")

finally:
  GPIO.cleanup()
