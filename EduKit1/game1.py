import time
from datetime import datetime
import random
from gpiozero import LED, Button, Buzzer

leds = tuple(map(lambda x: LED(x), (18, 23, 24, 13, 16, 26)))

buzzer = Buzzer(22)
quiet_buzzer = leds[0]

button = Button(25)

print('Ready..')
time.sleep(1)
print('Steady..')
time.sleep(random.randint(1, 5))
print('Go!')

while True:
    for i in range(6):
        leds[i].on()
        if 0 == random.randint(0, 6):
            time_count = 0
            time.sleep(random.randint(1, 5))
            if button.is_pressed:
                print('Falstart!')
                leds[i].off()
                continue
            start = datetime.now()
            #quiet_buzzer.on() 
            buzzer.on()
            while not button.is_pressed:
                pass
            stop = datetime.now()
            #quiet_buzzer.off()
            buzzer.off()
            print('Reaction: {}s'.format((stop - start).total_seconds()))
        time.sleep(0.5)
        leds[i].off()



