# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code
import time  # Import the Time library
from gpiozero import CamJamKitRobot, Buzzer  # Import the GPIO Zero Library CamJam library
from evdev import InputDevice, categorize, ecodes

robot = CamJamKitRobot()
buzzer = Buzzer(16)

gamepad = InputDevice('/dev/input/event0')

def move(vertical, horizontal, last_vertical):
    if horizontal == 0 and vertical == 0:
        robot.stop()

    elif horizontal == 0:
        if vertical == -1:
            robot.forward()
        elif vertical == 1:
            robot.backward()

    elif horizontal == 1:
        if vertical == 0:
            # only right
            if last_vertical == 0 or last_vertical == -1:
                robot.left_motor.forward(1)
            elif last_vertical == 1:
                robot.left_motor.backward(1)
            robot.right_motor.stop()
        elif vertical == -1:
            # right + forward
            robot.left_motor.forward(1)
            robot.right_motor.forward(0.5)
        elif vertical == -1:
            # right + backward
            robot.left_motor.backward(1)
            robot.right_motor.backward(0.5)

    elif horizontal == -1:
        if vertical == 0:
            # only left
            if last_vertical == 0 or last_vertical == -1:
                robot.right_motor.forward(1)
            elif last_vertical == 1:
                robot.right_motor.backward(1)
            robot.left_motor.stop()
        elif vertical == -1:
            # left + forward
            robot.right_motor.forward(1)
            robot.left_motor.forward(0.5)
        elif vertical == 1:
            # left + backward
            robot.right_motor.backward(1)
            robot.left_motor.backward(0.5)


vertical = 0
last_vertical = 0
horizontal = 0


for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        if event.code == 16:
            horizontal = event.value
        elif event.code == 17:
            last_vertical = vertical
            vertical = event.value

    elif event.type == ecodes.EV_KEY:
        if event.code == 305:
            if event.value > 0:
                buzzer.on()
            else:
                buzzer.off()

    move(vertical, horizontal, last_vertical)

