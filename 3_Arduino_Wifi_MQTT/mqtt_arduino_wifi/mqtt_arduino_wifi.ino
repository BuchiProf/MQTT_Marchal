#include <ArduinoMqttClient.h>
#include <WiFiNINA.h>
#include "arduino_secrets.h"

///////enregistrer les données sensibles dans l'onglet/arduino_secrets.h
char ssid[] = SECRET_SSID;        // le nom du point d'acces wifi
char pass[] = SECRET_PASS;    // le mot de passe du point d'acces wifi

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[] = "192.168.1.210";    //l'adresse ip du BROKER MQTT
int        port     = 1883;
const char topic[]  = "topic_1";          //déclaration des topic sur lesquelles on peut souscrire
const char topic2[]  = "topic_2";
//const char topic3[]  = "topic_x";

//interval d'envoi des messages (millisecondes)
const long interval = 8000;
unsigned long previousMillis = 0;

int count = 0;

/*********************************************************/
void setup() {
  
  Serial.begin(9600);
  while (!Serial) {
    ; // attente de connexion au port série
  }

  // tentative de connexion au wifi:
  Serial.print("Connexion en cours au point d'accès wifi : ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // erreur, recommence
    Serial.print(".");
    delay(5000);
  }

  Serial.println("Connexion au point d'accès réussie");
  Serial.println();
// Vous pouvez fournir un nom de client unique (obligatoire pour notre Broker), sinon le programme utilise Arduino-millis()
// mqttClient.setId("IdClientPerso");

  // Définition de l'identifiant et mot de passe du Broker MQTT
  mqttClient.setUsernamePassword(SECRET_BROKER, SECRET_BROKER_PASS);
  Serial.print("Connexion au Broker MQTT : ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("Erreur de connexion au Broker! Code d'erreur = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("Vous êtes connecté au Broker MQTT!");
  Serial.println();
}

/*****************************************************/
void loop() {
  // poll() permet de maintenir la connexion au Broker
  // si aucun message n'est envoyé régulièrement
  mqttClient.poll();

  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // envoi des messages périodiquement (interval a été défini à 8s)
    previousMillis = currentMillis;

    //on lit des valeurs au hasard sur les entrées A0 et A1 pour l'exemple
    int Rvalue = analogRead(A0);
    int Rvalue2 = analogRead(A1);
   
    Serial.print("Envoi du message vers le topic : ");
    Serial.println(topic);
    Serial.println(Rvalue);

    Serial.print("Envoi du message vers le topic : ");
    Serial.println(topic2);
    Serial.println(Rvalue2);

   

    // envoi du message à l'aide d'une fonction print
    mqttClient.beginMessage(topic);
    mqttClient.print(Rvalue);
    mqttClient.endMessage();

    mqttClient.beginMessage(topic2);
    mqttClient.print(Rvalue2);
    mqttClient.endMessage();

    Serial.println();
  }
}
