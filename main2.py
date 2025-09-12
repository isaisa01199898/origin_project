import sys
sys.path.append('/bin')
sys.path.append('/etc')

import machine

machine.Pin(4, machine.Pin.IN)

green_led = machine.Pin(5, machine.Pin.OUT)
green_led.value(1)

blue_led = machine.Pin(21, machine.Pin.OUT)
blue_led.value(1)

from al.hub import led
led.off()

from esp32 import Partition
Partition.mark_app_valid_cancel_rollback()
