from machine import I2C, Pin
import utime

from .ccs811 import CCS811, CCS811_ADDR
from .lcd import LCD, AQM1602_ADDR
from .sk1812mini import SK1812
from .wifi import WIFI
from .post import SimplePostServer
from . import parameters


class AirMonitor:
    def __init__(self):
        sda = Pin(21)
        scl = Pin(22)
        self._i2c = I2C(0, sda=sda, scl=scl, freq=10_000)
        # self._lcd_i2c = I2C(1, sda=Pin(6), scl=Pin(7))
        self._lcd_i2c = self._i2c
        self._css811 = CCS811(self._i2c)
        self._display = LCD(self._lcd_i2c)
        self._indicator = SK1812(Pin(16, mode=Pin.OUT))
        self._wifi = WIFI(parameters.SSID, parameters.WIFI_PASSWORD)
        self._post = SimplePostServer(parameters.RECORDER_HOST, parameters.TARGET, parameters.AUTH)

    def setup(self) -> bool:
        print("start setup")
        self._indicator.setup()
        self._indicator.yellow()

        print("setup display")
        i2c_addrs = self._lcd_i2c.scan()
        if AQM1602_ADDR not in i2c_addrs:
            self._indicator.red()
            raise Exception("cannot use display lcd")
        self._display.setup()
        self._display.print("setuping...")

        for i in range(5):
            print("setup CCS811 {}/{}".format(i + 1, 5))
            i2c_addrs = self._i2c.scan()
            if CCS811_ADDR not in i2c_addrs:
                self._indicator.red()
                self._display.print("fail i2c.scan", "CCS811")
                utime.sleep(5)
                continue
            try:
                self._css811.setup()
                self._display.print("setup done")
            except OSError:
                print("css811 setup failed")
                utime.sleep(5)
            break
        else:
            print("all css811 setup failed")
            return False
        self._wifi.up()
        print("setup done")
        utime.sleep(3)
        return True

    def loop(self):
        self._indicator.dark_blue()
        i = 0
        while True:
            print("try", i)
            i += 1
            data_available = False
            r = (0, 0)
            try:
                data_available = self._css811.data_available()
                if data_available:
                    r = self._css811.read_algorithm_results()
            except OSError as e:
                # self._indicator.yellow()
                print("error on CCS811", e)
                utime.sleep(5)
            if data_available:
                l1 = "CO2 : {:5d}-{:4d}".format(r[0], i%100)
                l2 = "tVOC: {:5d}".format(r[1])
                print(l1, l2)
                try:
                    utime.sleep_ms(200)
                    self._display.print(l1, l2)
                    if r[0] > 1200:
                        self._indicator.red()
                    else:
                        self._indicator.dark_blue()

                    self._wifi.up()
                    self._post.post({
                        "co2": r[0],
                        "t_voc": r[1],
                    })

                except OSError as e:
                    utime.sleep_ms(100)
                    # self._indicator.yellow()
                    print("error on display", e)
                    self._display.setup()
                    self._display.print(l1, l2)
                    utime.sleep(1)
                    self._display.print(l1, l2)
            utime.sleep(5)


def main():
    global m
    m = AirMonitor()
    try:
        m.setup()
    except Exception as e:
        print(e)
        utime.sleep(10)
        return
    m.loop()