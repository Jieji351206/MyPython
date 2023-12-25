from machine import Pin, PWM, ADC
import time

pwm = PWM(Pin(2))

adc = ADC(Pin(15))

pwm.freq(1000)


while True:
    duty = adc.read_u16()
    print("Analog Value:", duty)
    time.sleep(0.1)
    pwm.duty_u16(duty)
