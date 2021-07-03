import utime
import network

class WIFI:
    def __init__(self, ssid: str, password: str):
        self._ssid = ssid
        self._password = password
        self._wifi = network.WLAN(network.STA_IF)

    def up(self):
        while True:
            if not self._wifi.active():
                self._wifi.active(True)
                utime.sleep(1)
            if not self._wifi.isconnected():
                self._wifi.connect(self._ssid, self._password)
                utime.sleep(5)
            if self._wifi.isconnected():
                break
            print("cannot connect wifi")
            utime.sleep(1)
