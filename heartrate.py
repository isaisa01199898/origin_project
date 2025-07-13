import serial
import csv
i=3
user_input= input("Enter the number of heartbeats to record: ")
print("starting recording heartbeats...")
with open('line.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['hearts'])

def heartrate():
    global i
    global sensor_data
    while True:
        ser = serial.Serial('com3',9600)
        data = []
        i+=1

        while len(data) < i:     #forではできない
            line = ser.readline().strip()
            data.append(line)
            
        ser.close()

        sensor_data = (data[-1])
        print(f"{sensor_data}")
        with open("line.csv", 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([f'{sensor_data}'])


heartrate()