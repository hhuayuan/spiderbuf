import machine
import time

# NodeMCU内置LED通常在GPIO2
led = machine.Pin(2, machine.Pin.OUT)
while True:
    led.on()  # 点亮LED
    time.sleep(1)
    led.off()  # 熄灭LED
    time.sleep(1)
