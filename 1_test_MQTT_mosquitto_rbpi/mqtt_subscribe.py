# coding: utf-8
""" Programme python basique pour une souscription 
    au topic "essai/#" sur le broker Mosquitto.
    On définit un nom de client car on n'autorise pas 
    les connexions anonymes dans le server Mosquitto   
"""

import paho.mqtt.client as mqtt_client

# Configuration 
MQTT_BROKER = "10.129.230.1"
MQTT_PORT   = 1883
KEEP_ALIVE  = 60 # interval en seconde
IDENTIFIANT = None
MDP = None

def on_log( client, userdata, level, buf ):
    """permet de voir les logs lors des échanges sur le stream"""
    print( "log: ",buf)

def on_connect( client, userdata, flags, rc ):
    print( "Connexion: code retour = %d" % rc )
    print( "Connexion: Statut = %s" % ("OK" if rc==0 else "échec") )


def on_message( client, userdata, message ):
    print( "Reception message MQTT..." )
    print( "Topic : %s" % message.topic )
    print( "Data  : %s" % message.payload )

# création d'un objet mqtt_client avec l'id Louis
client = mqtt_client.Client( client_id="Louis" )

# Assignation des fonctions de rappel
client.on_message = on_message
client.on_connect = on_connect
#client.on_log = on_log 

# Connexion broker
client.username_pw_set( username=IDENTIFIANT, password=MDP )
client.connect( host=MQTT_BROKER, port=MQTT_PORT, keepalive=KEEP_ALIVE )
client.subscribe( "essai/#" )

# Envoi des messages
client.loop_forever()

