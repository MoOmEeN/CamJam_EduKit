# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature
# Import Libraries
import time
from w1thermsensor import W1ThermSensor
from gpiozero import LED, Buzzer

sensor = W1ThermSensor()

red = LED(18)
blue = LED(24)
buzzer = Buzzer(22)

# Print out the temperature until the program is stopped.
while True:
    temp = sensor.get_temperature(W1ThermSensor.DEGREES_C)
    print(temp)
    if int(temp) < 5:
        blue.on()
    elif int(temp) > 60:
        red.on()
        if int(temp) > 75:
            buzzer.on()
    time.sleep(1)
    red.off()
    blue.off()
    buzzer.off()
