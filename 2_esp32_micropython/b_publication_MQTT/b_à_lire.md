# Publication des mesures du BME680 sur le broker MQTT

Dans cette partie nous allons nous connecter automatiquement au point d'accès wifi du réseau en mode station.

* ouvrir le fichier boot.py (fichier exécuté au démarrage de l'ESP32) et modifier le nom et le mdp de votre point d'accès wifi.
* enregistrer ce fichier sur l'esp32 (`enregistrer sous --> Appareil MicroPython`)

Le programme principal permet de se connecter au Broker MQTT et de publier la température, l'humidité et la pression atmosphérique dans 3 topics : maison/extérieur/tmp, maison/extérieur/hr, maison/extérieur/pr
