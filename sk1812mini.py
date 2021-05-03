import array, time
from machine import Pin
import rp2

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def _ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


class SK1812:
    def __init__(self, gpio: Pin):
        self._sm = rp2.StateMachine(0, _ws2812, freq=8_000_000, sideset_base=gpio)
        self._sm.active(1)

    def set_color(self, r:int, g:int, b:int):
        ar = array.array("I", [0])
        ar[0] = g << 16 | r << 8 | b
        self._sm.put(ar, 8)

def main():
    led = SK1812(Pin(17))
    for i in range(100):
        if i % 3 == 0:
            led.set_color(25, 0, 0)
        elif i % 3 == 1:
            led.set_color(0, 25, 0)
        else:
            led.set_color(0, 0, 25)
        time.sleep(1)