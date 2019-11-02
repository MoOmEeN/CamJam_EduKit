# CamJam EduKit 2 - Sensors (GPIO Zero)
# Worksheet 4 - Light
# Import Libraries
from gpiozero import LED, Buzzer, LightSensor
import time

# A variable with the LDR reading pin number
ldr = LightSensor(27)

red = LED(18)
blue = LED(24)
buzzer = Buzzer(22)


while True:
    light = int(ldr.value * 100)
    print(light)
    if light < 10:
        blue.on()
    if light > 70:
        red.on()
    if light > 80:
        buzzer.on()
    time.sleep(1) # Wait for a second
    red.off()
    blue.off()
    buzzer.off()
