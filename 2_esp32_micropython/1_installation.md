# Installation du firmware micropython à l'aide de Thonny

* télécharger la dernière version ici : https://micropython.org/download/esp32/
* télécharger et installer Thonny : https://thonny.org/

    * Dans Thonny, choisir l'interpréteur `ESP32 micropython` (Menu `éxécuter --> configurer l'interpréteur`),

    *  Cliquer en bas à droite sur `installer ou mettre à jour le firmware`,
    * Indiquer le `port`et le `firmware`que vous avez téléchargé,
    * tout en restant appuyé sur le bouton **boot** de votre ESP32, cliquer sur `installer`,
    * relâcher le bouton **boot** dès que la procédure d'installation démarre.
* Tester que tout s'est bien passé en allant dans la console (REPL) et allumer la DEL intégrée sur la broche 2 :  
> from machine import Pin  
> DEL = Pin(2, Pin.OUT)  
> DEL.value(1) # 0 pour éteindre