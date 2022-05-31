# Souscrire à TOUS les message avec "#"
#  -h le serveur mosquitto à contacter
#  -t le topic auquel on souscrit (utiliser # pour tous)
#  -v verbose (mode bavard : ajoute le nom du topic en plus du message)
#  -u mosquitto user login (si défini dans le serveur mosquitto)
#  -P mosquitto user password (si défini dans le serveur mosquitto)
#
# exemple de souscrition à TOUS les message sur un serveur mosquitto non protégé
mosquitto_sub -h 10.129.230.1 -t "#" -v



#   Ajout de l'utilitaire ts pour afficher la date et l'heure en sortie
#   (ts peut nécessiter une installation "sudo apt install moreutils") 
#
#mosquitto_sub -h 10.129.230.1 -t "#" -v -u pusr103 -P 21052017 | ts


