import time
import random
import serial
import openai
import cv2

# シリアルポートを設定
ser = serial.Serial('com8', 9600)  # 9600はArduinoと同じボーレート

print("ログインを始めます")
age = int(input("年齢を入力してください: "))
maxHR = 220 - age  # 最大心拍数最大心拍数
study_zoneHRmin = maxHR * 0.6 # 勉強中のゾーン心拍数（最小）
study_zoneHRmax = maxHR * 0.7 # 勉強中のゾーン心拍数（最大）
HR_AB = maxHR * 1.21      

line_count = 0  

while True:
    if ser.in_waiting > 0:
        sensor_data = ser.readline().decode('utf-8').strip()  # Arduinoからのデータを読み取る
        line_count += 1  # 行数をカウント

        if line_count == 14:  # 14行目のデータを取得
            try:
                sensor_data = float(sensor_data)  # 数値に変換
            except ValueError:
                print(f"無効なデータ: {sensor_data}")
                continue

            print(f"{sensor_data}")

            if study_zoneHRmin < sensor_data < study_zoneHRmax:
                print("心拍数は勉強中のゾーンに入っています。")
                # ここに心拍数が勉強中のゾーンに入っている場合の処理を追加
            elif sensor_data > HR_AB:
                print("心拍数が高すぎます。")
                # ここに心拍数が高すぎる場合の処理を追加
            elif study_zoneHRmax  < sensor_data:
                print("心拍数が勉強中のゾーンを超えています。")
                # ここに心拍数が勉強中のゾーンを超えている場合の処理を追加
            elif sensor_data < study_zoneHRmin:
                print("心拍数が勉強中のゾーンを下回っています。")
                # ここに心拍数が勉強中のゾーンを下回っている場合の処理を追加 
                break