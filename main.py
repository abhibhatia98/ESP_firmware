from ota_updater import OTAUpdater
import machine
import utime

pin2 = machine.Pin(2, machine.Pin.OUT)

def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/abhibhatia98/ESP-OTA-UPDATER')
    o.download_and_install_update_if_available('MOTO', '12345678')


def start():
    while 1:
        pin2.value(1)
        utime.sleep_ms(500)
        pin2.value(0)
        utime.sleep_ms(500)
    
     


def boot():
    print("come in boot")
    print("calling download_and_install_update_if_available")
    download_and_install_update_if_available()
    print("calling start")
    start()

boot()