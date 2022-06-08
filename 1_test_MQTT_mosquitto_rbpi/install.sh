#installation du broker mosquitto sur la raspberry pi

#on met à jour la distribution
sudo apt-get update
sudo apt-get upgrade
#on peut redémarrer (conseillé)
sudo reboot
#installation du broker (déjà inclus dans l'os du rbpi)
sudo apt-get install mosquitto
#installation du client mosquitto
sudo apt-get install mosquitto-clients
# on en profite pour inclure la bibliothèque python
sudo apt-get install python3-pip
sudo pip install paho-mqtt
