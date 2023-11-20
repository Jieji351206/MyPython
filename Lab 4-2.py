from machine import Pin
from time import sleep
import dht
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

sensor =dht.DHT22(Pin(13))
# use I2C1 and GPIO 14,15 for SDA and SCL pins
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
dev_addr_list = i2c.scan() # scan I2C devices 
for addr in dev_addr_list:
    print('Found: 0x{:02x}'.format(addr) )
    
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    oled = SSD1306_I2C( 128, 32, i2c, addr=0x3c)
    oled.fill(0)
    oled.text("Tem:{}°C".format(temp),5,5)
    oled.text("Hum:{}%".format(hum),5,15)
    oled.show()
    print("Temperature:{0}°C Humidity:{1}% ".format(temp,hum))
    sleep(2)
