from machine import Pin

class DHT11():
    def __init__(self, pin: Pin): ...
    def measure(self)->None: ...
    def temperature(self)->int: ...
    def humidity(self)->int: ...