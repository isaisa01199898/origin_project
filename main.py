from machine import Pin
from config import BUTTON
import config
pin = Pin(BUTTON, Pin.IN)

import voltage
import _thread

if (pin.value() == 0):
    config.communication_path = 'bluetooth'

    import ubinascii
    mac = ubinascii.hexlify(machine.unique_id()).decode()

    from blerepl import init, start_advertise, run
    init()
    start_advertise(mac)

    run()

else:
    machine.freq(80000000)
    config.communication_path = 'wired'

    import config_manager as cm

    st = cm.read('st')
    if st == 'testmode':
        pass    
    else:
        import usr.user_program
