import serial
import time

# SPIKE の COM ポートを指定（例：COM5）
ser = serial.Serial("COM5", 115200, timeout=1)

# コマンド送信（例：LEDを赤に）
ser.write(b'hub.light_matrix.show_image(\"HEART\")\r')

# 少し待機（反応時間のため）
time.sleep(1)

# 通信を閉じる
ser.close()
