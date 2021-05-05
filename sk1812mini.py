import array, time
from machine import Pin
import neopixel


class SK1812:
    def __init__(self, gpio: Pin):
        self._np = neopixel.NeoPixel(gpio, 1)

    def setup(self):
        pass

    def set_color(self, r: int, g: int, b: int):
        self._np[0] = (r, g, b, 129)
        self._np.write()

    def yellow(self):
        self.set_color(0xFF, 0xF1, 0x00)

    def dark_yellow(self):
        self.set_color(0x10, 0x10, 0x00)

    def dark_blue(self):
        self.set_color(0x00, 0x00, 0x20)

    def red(self):
        self.set_color(0xFF, 0x00, 0x00)


def main():
    led = SK1812(Pin(16))
    led.setup()
    for i in range(100):
        if i % 3 == 0:
            led.set_color(255, 0, 0)
        elif i % 3 == 1:
            led.set_color(0, 255, 0)
        else:
            led.set_color(0, 0, 255)
        time.sleep(1)