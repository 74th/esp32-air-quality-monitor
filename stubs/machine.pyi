from typing import Any, Dict, Optional, Sequence, Tuple, Union

Node = Any

class ADC:
    def atten() -> None: ...
    def read() -> None: ...
    def read_u16() -> None: ...
    def width() -> None: ...

class DAC:
    def write() -> None: ...

class I2C:
    def __init__(self, no: int, sda: Pin, scl: Pin, freq: int): ...
    def init() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def readinto() -> None: ...
    def scan() -> list[int]: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
    def writevto() -> None: ...

class PWM:
    def __init__(self, pin: Pin, freq: int = 1024, duty: int = 0): ...
    def deinit(self) -> None: ...
    def duty(self, int) -> None: ...
    def freq(self, int) -> None: ...
    def init(self, int) -> None: ...

class Pin:
    IN = 1
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    PULL_DOWN = 1
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4
    def __init__(self, no: int, mode: int = Pin.OUT): ...
    def init() -> None: ...
    def irq() -> None: ...
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

class RTC:
    def datetime() -> None: ...
    def init() -> None: ...
    def memory() -> None: ...

class SDCard:
    def deinit() -> None: ...
    def info() -> None: ...
    def ioctl() -> None: ...
    def readblocks() -> None: ...
    def writeblocks() -> None: ...

class SPI:
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...

class Signal:
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

class SoftI2C:
    def init() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def readinto() -> None: ...
    def scan() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
    def writevto() -> None: ...

class SoftSPI:
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...

class Timer:
    def deinit() -> None: ...
    def init() -> None: ...
    def value() -> None: ...

class TouchPad:
    def config() -> None: ...
    def read() -> None: ...

class UART:
    def any() -> None: ...
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def sendbreak() -> None: ...
    def write() -> None: ...

class WDT:
    def feed() -> None: ...

def deepsleep() -> None: ...
def disable_irq() -> None: ...
def enable_irq() -> None: ...
def freq() -> None: ...
def idle() -> None: ...
def lightsleep() -> None: ...
def reset() -> None: ...
def reset_cause() -> None: ...
def sleep() -> None: ...
def soft_reset() -> None: ...
def time_pulse_us() -> None: ...
def unique_id() -> None: ...
def wake_reason() -> None: ...
