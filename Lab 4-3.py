from machine import Pin
from time import sleep
import dht
import max7219
from machine import Pin, SPI
from time import sleep

sensor =dht.DHT22(Pin(13))

num_display = 4

cs_pin = Pin(5, Pin.OUT)

spi = SPI(0)

display = max7219.Matrix8x8(spi, cs_pin, num_display)

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    display.fill(0)
    display.text("{}°C".format(temp),0,1,1)
    display.show()
    sleep(3)
    
    display.fill(0)
    display.text("{}%".format(hum),0,1,1)
    display.show()
    sleep(3)
