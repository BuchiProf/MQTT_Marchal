""" Simple lecture des capteurs du BME680 (Température, humidité, pression et gas)
    Module GROVE BME680
    Buchi S (mai 2022)
"""
# Projet inspiré du site https://RandomNerdTutorials.com/micropython-bme680-esp32-esp8266/

from machine import Pin, SoftI2C
from time import sleep
from bme680 import *

# ESP32 - configuration broches I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))


bme = BME680_I2C(i2c=i2c)

while True:
  try:
    temp = str(round(bme.temperature, 2)) + ' C'

    
    hum = str(round(bme.humidity, 2)) + ' %'
    
    pres = str(round(bme.pressure, 2)) + ' hPa'
    
    gas = str(round(bme.gas/1000, 2)) + ' kOhms'

    print('Temperature:', temp)
    print('Humidité:', hum)
    print('Pression atmo:', pres)
    print('Gas:', gas)
    print('-------')
  except OSError as e:
    print('Erreur lecture capteur.')
 
  sleep(5)
