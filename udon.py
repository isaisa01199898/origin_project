
import threading
import time
import asyncio
import cv2
import dlib
import gaze_tracking.tracking as gt
from gaze_tracking.tracking import GazeTracking
import os
import datetime
import csv
import sys
import time 
import pprint
import keyboard
import serial
csv_file = 'line.csv'
#ーー変数一覧ーー#
text=None
datatime = None
left_x_box=[]
left_y_box=[]
right_x_box=[]
right_y_box=[]
left_eye_x=[]
left_eye_y=[]
eye_data = []
right_eye_x=[]
right_eye_y=[]
flat_list_left_x=[]
flat_list_left_y=[]
flat_list_right_x=[]
flat_list_right_y=[]
left_pupil_x = None
left_pupil_y = None
right_pupil_x = None
right_pupil_y = None
text = None
left_pupil = None
right_pupil = None
sor_data = 0.0
i=40
rine = 0.0
jude =""
sensor_data=""#心拍数のデータ
gaze_data = None
gaze= None
count=0
kigou=""#目線での判定結果
#ーー変数一覧ーー#

with open ('line.csv', 'a', encoding='UTF-8')as f:
    print("syoki")
    writer = csv.writer(f)
    f.truncate(0)  # ファイルを空にする


def judement():
    if kigou == "maru" and  70 <= sensor_data <= 80:
        jude = "focus"
    
        print(jude)   

    elif kigou == "batu" and  sensor_data < 70: 
        print("not focus very much")
    
    else :
        print("not focus")

def eye_do():
    import gaze_tracking.gaze_tracking as gt
    left_pupil_x = None
    left_pupil_y = None
    count=0

    right_pupil_x = None
    right_pupil_y = None
    text = None
    left_pupil = None
    right_pupil = None
    print("eye_do_strat")
    
        # class eye_tracking(object):
        #     print("haireta")
        #     # with open('line.csv', 'w', encoding='UTF-8')as f:
        #     #     writer = csv.writer(f)
        #     #     print("eye_tracking")
        #     #     writer.writerow(['左目のx座標','左目のy座標','右目のx座標','右目のy座標','方向','右目の座標','左目の座標'])
            
    print(gt.__file__)
    print(">>> loading GazeTracking from:", gt.__file__)
    print(">>> available methods:", [m for m in dir(gt.GazeTracking) if not m.startswith("_")])
    
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("未接続")
        exit()
    
    i = 0
    _, frame = webcam.read()
    # print(frame.shape, frame.dtype)
    # 確認
    gaze.refresh(frame)
    
    # print("frame before refresh:", frame.shape, frame.dtype)

    # 顔＋瞳に十字線を描画した結果を取得
    frame = gaze.annotated_frame()

    print(left_pupil_x  )
    print( left_pupil_y )
    print(right_pupil_x)  
    print(right_pupil_y) 
    print(text)
    print(right_pupil  )
    print(left_pupil)

    text = " "
    print("gaze:", gaze)


    
    while True:
        print("kurikaesi")
        # 0→瞬き　1→真ん中　2→右　3→左
        text = ""
            
        i = 0
        _, frame = webcam.read()

        
        # print("frame before refresh:", frame.shape, frame.dtype)
        
        # 顔＋瞳に十字線を描画した結果を取得
        frame = gaze.annotated_frame()
        if gaze.eye_left is not None and gaze.eye_right is not None:
            if gaze.eye_left.blinking is not None and gaze.eye_right.blinking is not None:
                if gaze.is_blinking():
                    text = "0"
                elif gaze.is_center():
                    text = "1"
                elif gaze.is_right():
                    text = "2"
                elif gaze.is_left():
                    text = "3"
            else:
                text = "未検出"  # 目が検出されていない場合の処理
        else:
            text = "未検出"  # 目が検出されていない場合の処理


    
        count+=1
        left_pupil_x = gaze.pupil_left_coords_x()
        left_pupil_y = gaze.pupil_left_coords_y()
        left_pupil = left_pupil_x,left_pupil_y
        right_pupil_x = gaze.pupil_right_coords_x()
        right_pupil_y = gaze.pupil_right_coords_y()
        right_pupil = right_pupil_x,right_pupil_y
        if left_pupil_x is not None and right_pupil_x is not None and left_pupil_y is not None and right_pupil_y is not None  :
            print("hai")
            csv_file = open('line.csv', 'r', encoding='ms932')
            f=csv.reader(csv_file, delimiter=',', doublequotechar=True, lineterminator='\n', quotechar='"', skipinitialspace=True)
            csv_file.close()
            print(f)
            print(f'{left_pupil_x}',f'{left_pupil_y}', f'{right_pupil_x}',f'{right_pupil_y}',f'{text}',f'{right_pupil}',f'{left_pupil}')
            return left_pupil_x,left_pupil_y, right_pupil_x,right_pupil_y,text,right_pupil,left_pupil
            break
        else:
            print("mouikkai")







def  reader():
    print("reader_start")
    if not os.path.exists(csv_file):
        print(f"{csv_file} が存在しません。")
        exit()
    with open ('line.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        print("初期化")
    previous_size = os.path.getsize(csv_file)




    while True:
        i=1
        previous_size = os.path.getsize(csv_file)
        current_size= previous_size

        while True:
            time.sleep(1)  # 1秒待機
            current_size = os.path.getsize(csv_file)
            if current_size != previous_size:
                print("ファイルサイズが変化しました！")
                break
            else:
                print("変化なし。監視中...")
                if keyboard.is_pressed('q'):
                    break
            previous_size = current_size  # 更新を忘れずに！
            if keyboard.is_pressed('q'):
                break

        with open('line.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            for left_x in reader:
                del left_x[-5:]
                left_x_box.append([int(value) for value in left_x if value])  # 数値に変換
        
        lis = list(filter(None, left_x_box))
        print(f"lis:{lis}")
        flat_list_left_x = [item for sublist in left_x_box for item in sublist]
        left_eye_x= [flat_list_left_x[j] - flat_list_left_x[j + 1] for j in range(len(flat_list_left_x) - 1)]
        with open('line.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            for left_y in reader:
                del left_y[-4:]
                del left_y[:1]
                left_y_box.append([int(value) for value in left_y if value])  # 数値に変換
        
        
        lis = list(filter(None, left_y_box))
        flat_list_left_y = [item for sublist in left_y_box for item in sublist]
        left_eye_y = [flat_list_left_y[j] - flat_list_left_y[j + 1] for j in range(len(flat_list_left_y) - 1)]
        
        with open('line.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            for right_x in reader:
                del right_x[-4:]
                del right_x[:2]
                right_x_box.append([int(value) for value in right_x if value])  # 数値に変換
        
        lis = list(filter(None, right_x_box))
        flat_list_right_x = [item for sublist in right_x_box for item in sublist]
        right_eye_x = [flat_list_right_x[j] - flat_list_right_x[j + 1] for j in range(len(flat_list_right_x) - 1)]

        with open('line.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            # print("haireta")
            # print(reader)
            for right_y in reader:
                del right_y[-3:]
                del right_y[:3]
                # print("keseta")
                # print(right_y)
                right_y_box.append([int(value) for value in right_y if value])  # 数値に変換
        
        
        lis = list(filter(None, right_y_box))
        # print(lis)
        flat_list_right_y = [item for sublist in right_y_box for item in sublist]
        # print(len(flat_list_right_y))
        right_eye_y= [flat_list_right_y[j] - flat_list_right_y[j + 1] for j in range(len(flat_list_right_y) - 1)]

        print(f"left_eye_y: {left_eye_y}")
        print(f"left_eye_x: {left_eye_x}")
        print(f"right_eye_x: {right_eye_x}")
        print(f"right_eye_y: {right_eye_y}")
        if left_eye_x and left_eye_y and right_eye_x and right_eye_y is not None:
            if (max(left_eye_y, default=0) > 5 and max(left_eye_x, default=0) > 5 and
                max(right_eye_x, default=0) > 5 and max(right_eye_y, default=0) > 5):
                print("×")
                kigou="batu"
            else:
                print("〇")
                kigou="maru"
        if keyboard.is_pressed('q'):
            break


def heartrate():
        print("heart_rate_start")
        ser = serial.Serial('com8',9600)
        line=''
        i=0
        data=[]
        while len(data)<2:     #forではできない
            line = ser.readline().strip()
            data.append(line)

        
            print(data)
        ser.close()
        try:
            sensor_data = float(data[-1])
            print(f"{sensor_data}")

        except :
            sensor_data = None
            print("you lose")
        return sensor_data





# # メイン
def sensor_read():
    if __name__ == "__main__":
        print("◆スレッド:", threading.currentThread().getName())
        print('system開始。')
        # スレッドを作る

        while True:
            # スレッドの処理を開始
            thread1 = threading.Thread(target=(gaze:=eye_do()))
            thread2 = threading.Thread(target=(sor_data:=heartrate()))


            thread2.start()
            thread1.start()
        
        
            # スレッドの処理を待つ
            thread1.join()
            thread2.join()
            now_time = datetime.datetime.now()
            print(gaze)
            print(str(gaze))
            left_x= (str(gaze[0]))
            left_y= (str(gaze[1]))
            right_x=(str(gaze[2]))
            right_y=(str(gaze[3]))
            bun=(str(gaze[4]))
            right=(str(gaze[5]))
            left= (str(gaze[6]))
            print(left)
            print(type(left))
            print(type(sor_data))
            print(sor_data)
            with open('line.csv', 'a', encoding='UTF-8') as f:
                writer = csv.writer(f)
                writer.writerow([f'{left_x}',f'{left_y}', f'{right_x}',f'{right_y}',f'{bun}',f'{right}',f'{left}',f'{now_time}',f'{sor_data}'])
            if keyboard.is_pressed('q'):
                print("qが押されました。")
                break
            print('system終了。')
            print(f"kigou={kigou}")

sensor_read()