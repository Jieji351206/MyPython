from machine import Pin
import  time

p13 = Pin(13,Pin.OUT)
p14 = Pin(14,Pin.OUT)
p15 = Pin(15,Pin.OUT)
p16 = Pin(16,Pin.OUT)


while True:
    p13.on()
    p14.on()
    p15.on()
    p16.on()
    time.sleep_ms(500)
    p13.off()
    p14.off()
    p15.off()
    p16.off()
    time.sleep_ms(500)