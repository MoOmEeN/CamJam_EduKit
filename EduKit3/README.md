## Robot car controlled with Joy-Con from Nintendo Switch

### Connecting Joy-Con to Raspberry
Followed https://raspberry-valley.azurewebsites.net/Map-Bluetooth-Controller-using-Python/

First enable **discovery mode on your Joy-Con** (press small button between SL and SR until lights start to blink)
```
# sudo bluetoothctl
[bluetooth]# scan on
[bluetooth]# devices (find Joy-Con)
[bluetooth]# pair XX:XX:XX:XX:XX:XX
[bluetooth]# connect XX:XX:XX:XX:XX:XX
Attempting to connect to XX:XX:XX:XX:XX:XX
[CHG] Device XX:XX:XX:XX:XX:XX Connected: yes
[CHG] Device XX:XX:XX:XX:XX:XX Paired: yes
Connection successful
```


Check device name
```
# ls /dev/input/event*
/dev/input/event0
```

### Finding Joy-Con event codes
```
# evtest 
Available devices:
/dev/input/event0:      Joy-Con (R)
Select the device event number [0-0]:
> 0
> (...)
> Testing ... (interrupt to exit)
```
Press buttons and observe the output, e.g.
```
Event: time 1573424584.634931, type 3 (EV_ABS), code 17 (ABS_HAT0Y), value 1
Event: time 1573424584.634931, -------------- SYN_REPORT ------------
Event: time 1573424584.739953, type 3 (EV_ABS), code 17 (ABS_HAT0Y), value 0
Event: time 1573424584.739953, -------------- SYN_REPORT ------------
Event: time 1573424656.995360, type 4 (EV_MSC), code 4 (MSC_SCAN), value 90002
Event: time 1573424656.995360, type 1 (EV_KEY), code 305 (BTN_EAST), value 0
Event: time 1573424656.995360, -------------- SYN_REPORT ------------
```
