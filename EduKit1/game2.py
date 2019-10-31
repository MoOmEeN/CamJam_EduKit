import time
from datetime import datetime
import random
from gpiozero import LED, Button, Buzzer

leds = tuple(map(lambda x: LED(x), (18, 23, 24, 13, 16, 26)))
yellow_idx = (1, 4)

button = Button(25)

success_count = 0
fail_count = 1

name = input("What is your name? ")

print('Ready..')
time.sleep(1)
print('Steady..')
time.sleep(random.randint(1, 5))
print('Go!')

for z in range(60):
    rand = random.randint(0, 5)
    leds[rand].on()
    success = False
    if rand in yellow_idx:
        w = datetime.now()
        while not button.is_pressed and (datetime.now() - w).total_seconds() < 0.5:
            pass
        if button.is_pressed:
            print('success')
            success_count = success_count + 1
        else:
            print('fail')
            fail_count = fail_count + 1
    else:
        time.sleep(0.5)
    leds[rand].off()

print('{}\'s score is {}%'.format(name, round(success_count/(success_count + fail_count) * 100)))
