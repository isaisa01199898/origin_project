import serial
ser = serial.Serial('COM3', 9600, timeout=5) #シリアルポートの設定
i=0
sensor_data=0
data=[]

def heartrate():
    global i
    global sensor_data
    global ser
    global data

    i+=1
    while len(data) < i:   
        line = ser.readline().strip()
        line = line.decode('utf-8', errors='ignore') 
        data.append(line)  #dataリストに心拍数データを格納 
    try:
        sensor_data = float(data[-1])  #dataリストから一番新しいデータを取得
        print(f"{sensor_data}")
    except ValueError:
        print("sippai")
        sensor_data = 0


while True:
    heartrate()