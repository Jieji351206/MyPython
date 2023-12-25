from machine  import Pin
import utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

red = Pin(16, Pin.OUT)
green = Pin(18, Pin.OUT)
blue = Pin(20, Pin.OUT)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
dev_addr_list = i2c.scan() # scan I2C devices 
for addr in dev_addr_list:
    print('Found: 0x{:02x}'.format(addr) )


while True:
  oled = SSD1306_I2C( 128, 32, i2c, addr=0x3c)
  oled.fill(0)
  oled.text("BLUE",50,10)
  red.value(0)
  green.value(1)
  blue.value(1)
  oled.show()
  utime.sleep(1)
  
  oled.fill(0)
  oled.text("PURPLE",40,10)
  red.value(1)
  green.value(0)
  blue.value(1)
  oled.show()
  utime.sleep(1)
  
  oled.fill(0)
  oled.text("YELLOW",40,10)
  red.value(1)
  green.value(1)
  blue.value(0)
  oled.show()
  utime.sleep(1)
  