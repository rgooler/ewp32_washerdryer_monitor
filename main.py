import machine
import ssd1306
import network
from config import *

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

# Create stuff for the screen
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Output to the screen

oled.fill(0) 
oled.text('MicroPython on', 0, 0)
oled.text('an ESP32 with an', 0, 10)
oled.text('attached SSD1306', 0, 20)
oled.text('OLED display', 0, 30)
oled.show()

do_connect()
oled.fill(0) 
oled.text(wlan.ifconfig(), 0, 0)
oled.show()