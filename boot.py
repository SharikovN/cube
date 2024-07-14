#ALL LIBS
import machine
from machine import Pin, I2C, ADC
from apds9960.const import *
from apds9960 import uAPDS9960 as APDS9960
import neopixel 
from time import sleep
import network
import urequests
import json, ssd1306
from micropyserver import MicroPyServer
import sht3x

#FILES
import emoji, lights, loading

#PINS
oled_i2c = machine.SoftI2C(sda=machine.Pin(16), scl = machine.Pin(17))
oled = ssd1306.SSD1306_I2C(128, 64, oled_i2c)
np = neopixel.NeoPixel(Pin(5), 14)
adc = ADC(Pin(32), atten = ADC.ATTN_11DB)
bus = I2C(1, sda=Pin(25), scl=Pin(26))
apds = APDS9960(bus)
apds.setProximityIntLowThreshold(50)
apds.enableGestureSensor()
temp_i2c = machine.SoftI2C(scl=Pin(21), sda=Pin(19))
temp_sensor = sht3x.SHT31(temp_i2c)

#NETWORK SETTINGS 
ssid = "CROCguest"
password = "belgorod"
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected():
    sleep(0.1)

def light(request):
      t = (adc.read_uv()/1000000, adc.read_u16())
      text = f"Lightness: {t[0]}"
      server.send(text)
      emoji.joy(40)
      if t[0] < 1:
            while True:
                  if apds.isGestureAvailable():
                        motion = apds.readGesture()
                        if motion == 1:
                              lights.lamp()
                              emoji.normal(40)
                              break
                        elif motion == 2:
                              lights.no()
                              emoji.eyes_closed()
                              emoji.em_sleep()
                              break
            return

def sad1(request):
      mood('sad')
      server.send('ok')
      return

def joy1(request):
      mood('joy')
      server.send('ok')
      return

def cold(request):
      res = temp_sensor.get_temp_humi()
      if res[0] < 20.0:
            server.send("It's very cold in the room! CUBE may get sick, please set the temperature to at least 20 degrees.")
            mood('ill')
      else:
            server.send(str(res[0]))
            return

server = MicroPyServer()
server.add_route("/light", light)
server.add_route("/cold", cold)
server.add_route("/sad", sad1)
server.add_route("/joy", joy1)
 
# res_js = json.loads(res.text)
# light_stat = res_js[0]['light']
# print(light_stat)
# if light_stat is False:
#     for i in range(14):
#         np[i] = (0, 0, 0)
#     np.write()
# elif light_stat is True:
#     for i in range(14):
#         np[i] = (255, 0, 0)
#     np.write()

 
 
 
def mood(mud):
      if mud == 'joy':
            lights.state('joy')
            emoji.animate('joy')
      elif mud == 'normal':
            lights.state('normal')
            emoji.animate('normal')
      elif mud == 'ill':
            lights.state('ill')
            emoji.animate('ill')
      elif mud == 'sad':
            lights.state('sad')
            emoji.animate('sad')
# blink()
 
# for i in range(7):
#     np[i] = (139, 0, 255)
# np.write()
 

loading.loading(4000)

print('IP:', wlan.ifconfig()[0])
for i in range(14):
      np[i] = (0,0,0)
      np.write()
mood('normal')
server.start()