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


#on configure notre broker pour fonctionner sans identification ni mot de passe
#de même on authorise les connexions anonymes

#edition du fichier de config
sudo nano /etc/mosquitto/mosquitto.conf
#dans le fichier on rajoute (les deux lignes suivantes) le port du broker ainsi que les connexions anonymes
listener 1883
allow_anonymous true

#on sauvegarde et on ferme l'éditeur : ctrl + x puis "oui"

#on redémarre tout
sudo reboot
