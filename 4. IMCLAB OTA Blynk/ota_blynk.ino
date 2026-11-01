#define BLYNK_PRINT Serial
#include <WiFi.h>
#include <BlynkSimpleEsp32.h>
#include <ArduinoOTA.h>
#include "secrets.h"

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWi-Fi terhubung.");

  Blynk.config(BLYNK_AUTH_TOKEN);
  Blynk.connect();

  ArduinoOTA.setHostname("imclab-robot");
  ArduinoOTA.begin();

  Serial.println("OTA siap digunakan.");
}

void loop() {
  Blynk.run();
  ArduinoOTA.handle();
}
