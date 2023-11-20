from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# use I2C1 and GPIO 14,15 for SDA and SCL pins
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
dev_addr_list = i2c.scan() # scan I2C devices 
for addr in dev_addr_list:
    print('Found: 0x{:02x}'.format(addr) )

oled = SSD1306_I2C( 128, 32, i2c, addr=0x3c)
oled.fill(0)
oled.text("CDTI",5,5)
oled.text("6521061004",5,15)
oled.show()