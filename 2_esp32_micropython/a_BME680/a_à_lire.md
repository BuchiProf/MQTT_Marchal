# Premier programme sur ESP32 avec un capteur environnemental BME680
* Le module BME680 est connecté par I2C à l'ESP32 comme indiqué :  
  |BME280	| ESP32 |
  | ----- | ------ |
  |Vin	| 3.3V |
  |GND	| GND |
  |SCL	| GPIO 22 |
  |SDA	| GPIO 21 |  
* ouvrir les fichiers bme680.py (bibliothèque du capteur) et main.py (programme principal) avec Thonny
* enregistrer ces deux fichiers sur l'esp32 (`enregistrer sous --> Appareil MicroPython`)

* Executer le programme main.py et vous devriez voir dans la console des messages similaires à ci-dessous :  
> Temperature: 21.26 C  
> Humidité: 40.8 %  
> Pression atmo: 989.75 hPa  
> Gas: 25.57 kOhms
