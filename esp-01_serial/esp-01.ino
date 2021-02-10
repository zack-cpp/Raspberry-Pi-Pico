#include <ESP8266WiFi.h>

#define SSID "rumahkucing"
#define PASS  "1sl4m4g4m4ku"

String head = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
String html_1 = "<!DOCTYPE html><html><body><div id='main'>";
String html_2 = "<form id='F1' action='LEDON'></form><br>";
String html_3 = "<form id='F2' action='LEDOFF'></form><br>";
String html_4 = "</div></body></html>";

//#include <SoftwareSerial.h>
//SoftwareSerial serial(2,0); //D4 RX, D3 TX

String req;
String data;
void connectWiFi();

WiFiServer server(80);

void setup() {
  Serial.begin(9600);
//  serial.begin(9600);
  connectWiFi();
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if(!client){
    
  }else{
    //do after client connected
    req = client.readStringUntil('\r');
    req += '\n';
//    unsigned short int j = 0;
    for(int i = 5; i < req.length()-10; i++){
      data += req[i];
//      Serial.write(req[i]);
    }
    data += '\n';
    Serial.write(data.c_str());
    data = "";
//    Serial.write(req.c_str());
//    Serial.print("Web Data: ");
//    Serial.println(req);
    client.flush();
    client.print(head);
    client.print(html_1 );
    client.print(html_2 );
    client.print(html_3 );
    client.print(html_4);
  }
//  while(Serial.available()){
//    char s = Serial.read();
//    data += s;
//  }
//  if(data != ""){
//    Serial.print("Data: ");
//    Serial.println(data);
//  }
  
  delay(10);
}

void connectWiFi(){
  WiFi.begin(SSID, PASS);
  Serial.print("Connecting");
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }
  Serial.print("\nCOnnected to: ");
  Serial.println(SSID);
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}
