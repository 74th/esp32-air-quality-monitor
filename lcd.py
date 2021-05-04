from machine import I2C, Pin
import time

_AQM1602_ADDR = 0x3E


class LCD:
    def __init__(
        self,
        i2c: I2C,
    ):
        self._i2c = i2c
        self._init_lcd()
        self.clear()

    def _write_command(self, cmd: bytes):
        self._i2c.writeto(_AQM1602_ADDR, b"\x00" + cmd)
        time.sleep_ms(30)

    def print(self, line1: str, line2: str = ""):
        self.clear()
        buf = bytearray(b"\x40\x00")

        # カーソルを最初に
        self._write_command(b"\x80")
        for b in line1.encode():
            buf[1] = b
            self._i2c.writeto(_AQM1602_ADDR, buf)
        if len(line2) == 0:
            return

        # カーソルを2行目に
        self._write_command(b"\xc0")
        for b in line2.encode():
            buf[1] = b
            self._i2c.writeto(_AQM1602_ADDR, buf)

    def clear(self):
        self._write_command(b"\x01")

    def _init_lcd(self):
        time.sleep_ms(100)
        # Function set
        self._write_command(b"\x38")
        self._write_command(b"\x39")
        # Internal OSC frequency
        self._write_command(b"\x14")
        # Contrast set 1
        self._write_command(b"\x78")
        # Power/ICON/Contrast Control
        self._write_command(b"\x56")
        # Follow control
        self._write_command(b"\x6c")
        # Function set
        self._write_command(b"\x38")
        self._write_command(b"\x0c")
        self._write_command(b"\x01")
        self._write_command(b"\x06")


def test():
    sda = Pin(6)
    scl = Pin(7)
    i2c = I2C(1, sda=sda, scl=scl, freq=40000)
    lcd = LCD(i2c)

    lcd.print("aaaaa")
    time.sleep(3)
    lcd.print("hello world!", "@74th")
