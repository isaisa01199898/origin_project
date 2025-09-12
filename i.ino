#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"

MAX30105 particleSensor;

#define BEAT_THRESHOLD_MIN 100  // 最小しきい値
#define BEAT_THRESHOLD_MAX 20000  // 最大しきい値

long lastIRValue = -1;  // 前回のIR値
long lastBeat = 0;  // 最後のビート

const float FILTER_ALPHA = 0.95;  // フィルタ係数
long filteredIRValue = 0;

const byte RATE_SIZE = 50;   // 平均化のための配列サイズ
byte rates[RATE_SIZE];  
byte rateSpot = 0;
float bpm;
float beatAvg;
int beatCount = 0;
float sum = 0;
long irValue = 0;

// checkforBeat 関数(閾値の設定)
bool checkforBeat(long irValue) {
    if (irValue == 0) {
    return false;  // IR値が0の場合は無視
    }

    long delta = irValue - lastIRValue;

  // IR値を初期化  
    if (lastIRValue == -1) {
    lastIRValue = irValue;
    return false;  
    }

  // しきい値の設定
    if (delta > 100 && delta < 20000) {
    lastIRValue = irValue;  // ビート検出時にlastIRValueを更新
    return true;
    }
    return false;
}

void setup() {
    Wire.begin();
    Serial.begin(9600);
    particleSensor.begin(Wire, I2C_SPEED_FAST);
    particleSensor.setup();
    particleSensor.setPulseAmplitudeRed(0x0A);
}

int a;

void loop() {
    float irValue = 0;
    beatCount = 0;
    sum = 0;
    //  Serial.println("start");
    irValue = particleSensor.getIR();
    //  Serial.println(irValue);
    irValue = particleSensor.getIR();
      filteredIRValue = (FILTER_ALPHA * filteredIRValue) + ((1 - FILTER_ALPHA) * irValue);
      if (filteredIRValue > 200) { //低すぎる値をはじく
        if (checkforBeat(filteredIRValue)) {
          long currentMillis = millis();        //現在時間を取得
            long delta = currentMillis - lastBeat;//「二回目の拍動した時間」ー「一回目の拍動した時間」
            lastBeat = currentMillis;             //「一回目の拍動した時間」を更新
            if (delta > 0) {
                bpm = 60.0 / (delta / 1000.0);//deltaは一回当たりの拍動時間
                
            } else {
                bpm = 0;  // delta が 0 の場合を考慮
            }
            if (bpm >= 40 && bpm <= 225) {  // 正常な bpm の範囲内なら
                sum += bpm;
                Serial.println(bpm);
                beatCount++;
                a++;
            }
            } else {
            Serial.println("ビートが検出されませんでした。");
            }
        } else {
            Serial.println("指が検出されていません");
        }
        delay(700);
}


