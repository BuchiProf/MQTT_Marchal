# coding: utf8
""" Mesures avec BME680

	Envoi des données toutes les heures + 2 minutes
	vers serveur MQTT


 """

from machine import Pin, SoftI2C, reset
from time import sleep, time
from ubinascii import hexlify
from network import WLAN

CLIENT_ID = 'meteo'

# Adresse IP du Broker MQTT
# à modifier selon le cas

MQTT_SERVER = "192.168.1.210"

# Mettre le identifiants et mots de passe du Broker s'il y en a. Sinon None
MQTT_USER = None
MQTT_PSWD = None

# redemarrage auto après erreur
ERROR_REBOOT_TIME = 3600 # 1 h = 3600 sec


# --- Demarrage conditionnel ---
#décommenter si interrupteur sur broche 12
#runapp = Pin( 12,  Pin.IN, Pin.PULL_UP )
led = Pin(13, Pin.OUT)
led.value( 0 ) # eteindre


#décommenter si interrupteur
#if runapp.value() != 1:
#	from sys import exit
#	exit(0)

led.value( 1 ) # allumer

# --- Programme Pincipal ---
from umqtt.simple import MQTTClient
try:
    q = MQTTClient( client_id = CLIENT_ID, server = MQTT_SERVER, user = MQTT_USER, password = MQTT_PSWD )
    sMac = hexlify( WLAN().config( 'mac' ) ).decode()
    q.set_last_will( topic="disconnect/%s" % CLIENT_ID , msg=sMac )
    if q.connect() != 0:
        #led_error( step=1 )
        print("erreur 1")
except Exception as e:
    print( e )
    # check MQTT_SERVER, MQTT_USER, MQTT_PSWD
    #led_error( step=2 )
    print("erreur 2")

#essai d'import de la bibliothèque du capteur
try:
	from bme680 import *
except Exception as e:
	print( e )
	#led_error( step=3 )
	print("erreur 3")

# declare le bus i2c
i2c = SoftI2C( scl=Pin(22), sda=Pin(21) )

# créer les capteurs
try:
    bme = BME680_I2C(i2c=i2c)
except Exception as e:
    print( e )
    #led_error( step=4 )
    print("erreur 4")

try:
	# annonce connexion objet
	sMac = hexlify( WLAN().config( 'mac' ) ).decode()
	q.publish( "connect/%s" % CLIENT_ID , sMac )
except Exception as e:
	print( e )
	#led_error( step=5 )
	print("erreur 5")

import uasyncio as asyncio


def capture_2min():
	""" Executé pour capturer des donnees toutes les 2 mins """
	global q
	global bme
	# bme680 - capteur pression/température/humidité
	# capturer les valeurs sous format texte
	
	temp = str(round(bme.temperature, 2))
	hum = str(round(bme.humidity, 2))
	pres = str(round(bme.pressure, 2))
	q.publish( "maison/exterieur/tmp", temp )
	q.publish( "maison/exterieur/hr", hum )
	q.publish( "maison/exterieur/pr", pres )

def heartbeat():
	""" Led eteinte 200ms toutes les 10 sec """
	sleep( 0.2 )

async def run_every( fn, min= 1, sec=None):
	""" Execution asynchrone de tâches
	param : fonction, périodicité en min ou secondes"""
	global led
	wait_sec = sec if sec else min*60
	while True:
		# eteindre pendant envoi/traitement
		led.value( 0 )
		fn()
		led.value( 1 ) # allumer
		await asyncio.sleep( wait_sec )

async def run_app_exit():
	""" fin d'execution lorsque quitte la fonction """
	runapp=1
	while runapp==1:
		await asyncio.sleep( 10 )
	return

loop = asyncio.get_event_loop()

loop.create_task( run_every(capture_2min, min=2) )
loop.create_task( run_every(heartbeat, sec=10) )
try:
	loop.run_until_complete( run_app_exit() )
except Exception as e :
	print( e )
	#led_error( step=6 )
	print("erreur 6")

loop.close()
led.value( 0 ) # eteindre
print( "Fin!")
