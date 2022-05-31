# coding: utf-8
""" Programme python de base pour la
publication de données sur le topic "essai/#" du broker Mosquitto.
On définit un nom de client car on n'autorise pas 
les connexions anonymes dans le server Mosquitto.  
"""
import paho.mqtt.client as mqtt_client
from time import sleep

# Configuration 
MQTT_BROKER = "10.129.230.1"
MQTT_PORT   = 1883
KEEP_ALIVE  = 60 # interval en seconde
IDENTIFIANT = None
MDP = None


def on_log( client, userdata, level, buf ):
    """permet de voir les logs lors des échanges sur le stream"""
    print( "log: ",buf)

client = mqtt_client.Client( client_id="Louis" )

# A décommenter si on veut voir le flux du stream
#client.on_log = on_log 

# Connexion broker
client.username_pw_set( username=IDENTIFIANT, password=MDP )
client.connect( host=MQTT_BROKER, port=MQTT_PORT, keepalive=KEEP_ALIVE )

# envoi de 4 messages avec une pause de 1 seconde
for i in range(4):
    print( "Publication itération numpéro ",i )
    r = client.publish( "essai/bidule", "message", i )
    print( " bien envoyé" if r[0] == 0 else "  échec" ) 
    sleep( 1 )
