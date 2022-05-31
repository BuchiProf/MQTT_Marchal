# Envoyer un message vers le serveur mosquitto avec la commande mosquitto_pub
#  -h l'adresse du derveur mosquitto (privilégier l'adresse IP)
#  -t le topic auquel on souscrit (utiliser # pour tous)
#  -m le message à publier
#  -v verbose (mode bavard)
#  -u mosquitto user login (si défini dans le serveur mosquitto)
#  -P mosquitto user password (si défini dans le serveur mosquitto)
#
# exemple de publication sur le broker à l'adresse 10.129.230.1 du message 22 pour le topic ruche/temp
mosquitto_pub -h 10.129.230.1 -t "ruche/temp" -m 22 -u id_user -P mdp



# Le même message si l'on a pas choisi un serveur non protégé
#
# mosquitto_pub -h 10.129.230.1 -t "ruche/temp" -m 22
