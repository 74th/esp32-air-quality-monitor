import network

class wifi:
    def __init__(self, ssid: str, password: str):
        self._ssid = ssid
        self._password = password
        self._wifi = network.WLAN(network.AP_IF)

    def up(self):
        if not self._wifi.active():
            self._wifi.active(True)
        if not self._wifi.isconnected():
            self._wifi.connect(self._ssid, self._password)