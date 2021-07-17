from machine import Pin, PWM
import time

class FullColorLED:
    def __init__(self, r: Pin, g: Pin, b: Pin):
        self._r = PWM(r, freq=1024, duty=0)
        self._g = PWM(g, freq=1024, duty=0)
        self._b = PWM(b, freq=1024, duty=0)

    def set_color(self, r: int, g: int, b: int):
        self._r.duty(r*4)
        self._g.duty(g*4)
        self._b.duty(b*4)

    def yellow(self):
        self.set_color(0xFF, 0xF1, 0x00)

    def dark_yellow(self):
        self.set_color(0x10, 0x10, 0x00)

    def dark_blue(self):
        self.set_color(0x00, 0x00, 0x20)

    def red(self):
        self.set_color(0xFF, 0x00, 0x00)

def main():
    led = FullColorLED(Pin(12), Pin(14), Pin(27))
    for i in range(100):
        if i % 3 == 0:
            led.set_color(255, 0, 0)
        elif i % 3 == 1:
            led.set_color(0, 255, 0)
        else:
            led.set_color(0, 0, 255)
        time.sleep(1)