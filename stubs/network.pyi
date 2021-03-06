AP_IF = 1
AUTH_MAX = 8
AUTH_OPEN = 0
AUTH_WEP = 1
AUTH_WPA2_ENTERPRISE = 5
AUTH_WPA2_PSK = 3
AUTH_WPA_PSK = 2
AUTH_WPA_WPA2_PSK = 4
ETH_CONNECTED = 3
ETH_DISCONNECTED = 4
ETH_GOT_IP = 5
ETH_INITIALIZED = 0
ETH_STARTED = 1
ETH_STOPPED = 2

class LAN: ...
class PPP: ...

class WLAN:
    def __init__(self, wlan_if: int): ...
    def isconnected(self) -> bool: ...
    def active(self, active: bool = None) -> bool: ...
    def scan(self) -> list[tuple[bytes, bytes, int, int, int, bool]]: ...
    def connect(self, ssid: str, password: str): ...

def phy_mode() -> None: ...
