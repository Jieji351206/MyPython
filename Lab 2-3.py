from machine import Pin, PWM
from time import sleep

pwm1 = PWM(Pin(13))
pwm1.freq(10000)

pwm2 = PWM(Pin(14))
pwm2.freq(10000)

pwm3 = PWM(Pin(15))
pwm3.freq(10000)

pwm4 = PWM(Pin(16))
pwm4.freq(10000)

while True:
    for duty in range(65025):
        pwm1.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025):
        pwm2.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025):
        pwm3.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025):
        pwm4.duty_u16(duty)
        sleep(0.0001)
        
    for duty in range(65025, 0, -1):
        pwm1.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm2.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm3.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm4.duty_u16(duty)
        sleep(0.0001)

