
/*
 *
 * Arduino firmware to send and receive rf signals using serial port
 *
 */

#include <RCSwitch.h>
RCSwitch mySwitch = RCSwitch();

const int TXpin = 10;

String str;
String pulseLength;
String pulseCode;
String codeRepeat;

void setup() {
    Serial.begin(9600);
    mySwitch.enableTransmit(TXpin);
    delay(2000);
    Serial.println("Service started");
}

void loop() {

    if (Serial.available() > 0) {
        str = Serial.readString();

        if(str[0] == '#'){
            str.remove(0,1);

            pulseLength = getValue(str, ':', 0);
            pulseCode = getValue(str, ':', 1);
            codeRepeat = getValue(str, ':', 2);

            pulseCode.remove(0,2);
            codeRepeat.remove(codeRepeat.length()-2, 2);

            char pulseCodeArray[pulseCode.length()+1];
            pulseCode.toCharArray(pulseCodeArray, pulseCode.length()+1);

            char pulseLengthArray[pulseLength.length()+1];
            pulseLength.toCharArray(pulseLengthArray, pulseLength.length()+1);

            char codeRepeatArray[codeRepeat.length()+1];
            codeRepeat.toCharArray(codeRepeatArray, codeRepeat.length()+1);

            mySwitch.setPulseLength(atoi(pulseLengthArray));
            mySwitch.setRepeatTransmit(atoi(codeRepeatArray));
            mySwitch.sendRaw(pulseCodeArray, pulseCode.length()+1);
        }

    }
}

// http://arduino.stackexchange.com/questions/1013/how-do-i-split-an-incoming-string
String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

