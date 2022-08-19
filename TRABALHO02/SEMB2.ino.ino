// Load Wi-Fi library        //controle e acesso remoto
#include <WiFi.h>

// Replace with your network credentials
const char* ssid = "SEMB2";
const char* pass = "12345678";

// Set web server port number to 80
WiFiServer server(80);

const int pinoSensor = 34; //PINO UTILIZADO PELO SENSOR
float valorLido; //VARIÁVEL QUE ARMAZENA O PERCENTUAL DE UMIDADE DO SOLO

float analogSoloSeco = 3350; //VALOR MEDIDO COM O SOLO SECO (VOCÊ PODE FAZER TESTES E AJUSTAR ESTE VALOR)
float analogSoloMolhado = 1540; //VALOR MEDIDO COM O SOLO MOLHADO (VOCÊ PODE FAZER TESTES E AJUSTAR ESTE VALOR)
float percSoloSeco = 0; //MENOR PERCENTUAL DO SOLO SECO (0% - NÃO ALTERAR)
float percSoloMolhado = 100; //MAIOR PERCENTUAL DO SOLO MOLHADO (100% - NÃO ALTERAR)

// Variable to store the HTTP request
String header;

// Auxiliar variables to store the current output state
String bomba01estado = "DESLIGADA";
String bomba02estado = "DESLIGADA";
String led_salaestado = "DESLIGADA";

// Assign output variables to GPIO pins
const int bomba01 = 33; //33
const int bomba02 = 32;
const int led_sala = 2;

// Current time
unsigned long currentTime = millis();
// Previous time
unsigned long previousTime = 0; 
// Define timeout time in milliseconds (example: 2000ms = 2s)
const long timeoutTime = 2000;

#include "pagina.h"

void setup() {
  Serial.begin(115200);
  pinMode(bomba01, OUTPUT);
  pinMode(bomba02, OUTPUT);
  pinMode(led_sala, OUTPUT);
   
  digitalWrite(bomba01, LOW);
  digitalWrite(bomba02, LOW);
  digitalWrite(led_sala, LOW);

  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop(){

  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  
  valorLido = constrain(analogRead(pinoSensor),analogSoloMolhado,analogSoloSeco); //MANTÉM valorLido DENTRO DO INTERVALO (ENTRE analogSoloMolhado E analogSoloSeco)
  valorLido = map(valorLido,analogSoloMolhado,analogSoloSeco,percSoloMolhado,percSoloSeco); //EXECUTA A FUNÇÃO "map" DE ACORDO COM OS PARÂMETROS PASSADOS
 
  WiFiClient client = server.available();   // Listen for incoming clients

  if (client) {                             // If a new client connects,
    currentTime = millis();
    previousTime = currentTime;
    Serial.println("New Client.");          // print a message out in the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected() && currentTime - previousTime <= timeoutTime) {  // loop while the client's connected
      currentTime = millis();
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out the serial monitor
        header += c;
        if (c == '\n') {                    // if the byte is a newline character
          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
            
            // turns the GPIOs on and off
            if (header.indexOf("GET /bomba01/on") >= 0) {
              Serial.println("bomba 01 ligada");
              bomba01estado = "LIGADA";
              digitalWrite(bomba01, HIGH);      
            } else if (header.indexOf("GET /bomba01/off") >= 0) {
              Serial.println("bomba 01 desligada");
              bomba01estado = "DESLIGADA";
              digitalWrite(bomba01, LOW);
            }  
            if (header.indexOf("GET /bomba02/on") >= 0) {
              Serial.println("bomba 02 ligada");
              bomba02estado = "LIGADA";
              digitalWrite(bomba02, HIGH);      
            } else if (header.indexOf("GET /bomba02/off") >= 0) {
              Serial.println("bomba 02 desligada");
              bomba02estado = "DESLIGADA";
              digitalWrite(bomba02, LOW);
            }  
            if (header.indexOf("GET /led_sala/on") >= 0) {
              Serial.println("led_sala ligada");
              led_salaestado = "LIGADA";
              digitalWrite(led_sala, HIGH);      
            } else if (header.indexOf("GET /led_sala/off") >= 0) {
              Serial.println("led_sala desligada");
              led_salaestado = "DESLIGADA";
              digitalWrite(led_sala, LOW);
            }                           

            client.println(pagina);         
            
            // Display current state, and ON/OFF buttons for GPIO 26  
            client.println("<p>Bomba 1 " + bomba01estado + "</p>");
            // If the output26State is off, it displays the ON button       
            if (bomba01estado=="DESLIGADA") {
              client.println("<p><a href=\"/bomba01/on\"><button class=\"button\">Ligar</button></a></p>");
            } else {
              client.println("<p><a href=\"/bomba01/off\"><button class=\"button button2\">Desligar</button></a></p>");
            } 

            client.println("<p>Bomba 2 " + bomba02estado + "</p>");
            // If the output26State is off, it displays the ON button       
            if (bomba02estado=="DESLIGADA") {
              client.println("<p><a href=\"/bomba02/on\"><button class=\"button\">Ligar</button></a></p>");
            } else {
              client.println("<p><a href=\"/bomba02/off\"><button class=\"button button2\">Desligar</button></a></p>");
            } 

            client.println("<p>Iluminação " + led_salaestado + "</p>");
            // If the output26State is off, it displays the ON button       
            if (led_salaestado=="DESLIGADA") {
              client.println("<p><a href=\"/led_sala/on\"><button class=\"button\">Ligar</button></a></p>");
            } else {
              client.println("<p><a href=\"/led_sala/off\"><button class=\"button button2\">Desligar</button></a></p>");
            }            
            

            client.println("<p><h2>A umidade do solo está em:");
            client.println(valorLido);
            client.println("%</h2></p>");
            client.println(rodape);
            
            // The HTTP response ends with another blank line
            client.println();
            // Break out of the while loop
            break;
          } else { // if you got a newline, then clear currentLine
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }
      }
    }
    // Clear the header variable
    header = "";
    // Close the connection
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
    }
  }
