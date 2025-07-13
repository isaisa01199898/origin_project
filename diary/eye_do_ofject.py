from diary.gaze_tracking import GazeTracking
import diary.gaze_tracking.tracking as gt
import cv2
import dlib
import csv
import re
import time
import keyboard
import threading
import datetime
import os 
import serial
import csv
#ーー変数一覧ーー#
text=None
heart_data=None
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
left_pupil_x = 0
left_pupil_y = 0
right_pupil_x = 0
right_pupil_y = 0
text = 0
s= -1
m=8
line=''
i=3



data=[]
left_pupil = None
right_pupil = None
sor_data = 0.0
i=40
b=""
rine = 0.0
csv_file = 'line.csv'
jude =""
sensor_data=""#心拍数のデータ
gaze_data = None
gaze= None
left_pupil_x = None
left_pupil_y = None
right_pupil_x = None
right_pupil_y = None
right_pupil = None
left_pupil = None
heart_data = None
count=0
kigou=""#目線での判定結果
#ーー変数一覧ーー#
def data_get(left_pupil_x,left_pupil_y,right_pupil_x,right_pupil_y,right_pupil,left_pupil,heart_data):

    def eye_do():
        global left_pupil_x, left_pupil_y, right_pupil_x, right_pupil_y, right_pupil, left_pupil, heart_data
        global s, b, count  # ←ここにcountを追加

        while True:      
            with open ('line.csv', 'a', encoding='UTF-8') as f:
                print("syoki")
                writer = csv.writer(f)
                f.truncate(0)  # ファイルを空にする
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])
                writer.writerow([None,None,None,None,None,None,None,None])


                

            global s


            global b
            print("eye_do_strat")
            
                # class eye_tracking(object):
                #     print("haireta")
                #     # with open('line.csv', 'w', encoding='UTF-8')as f:
                #     #     writer = csv.writer(f)
                #     #     print("eye_tracking")
                #     #     writer.writerow(['左目のx座標','左目のy座標','右目のx座標','右目のy座標','方向','右目の座標','左目の座標'])
                    
            print(gt.__file__)
            # print(">>> loading GazeTracking from:", gt.__file__)
            # print(">>> available methods:", [m for m in dir(gt.GazeTracking) if not m.startswith("_")])
            
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

            gaze = GazeTracking()
            # 0→瞬き　1→真ん中　2→右　3→左
            text = ""
                
            i = 0
            _, frame = webcam.read()
            if frame is None:
                print("カメラからフレームが取得できませんでした")
                
            gaze.refresh(frame)
            
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
            if left_eye_x and left_eye_y and right_eye_x and right_eye_y and right_pupil and left_pupil and text is not None:
                print(f'{left_pupil_x}',f'{left_pupil_y}', f'{right_pupil_x}',f'{right_pupil_y}',f'{text}',f'{right_pupil}',f'{left_pupil}')
                print("書き込み完了")
                s -= 1
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
        global heart_data

        print("heart_rate_start")
        ser = serial.Serial('com3',9600)
        data = []
        while len(data) < i:     #forではできない
            line = ser.readline().strip()
            data.append(line)
            print(data)
            
        ser.close()


        try:
            heartrate = float(data[-1])
            print(f"{heartrate}")
            with open('line.csv', 'a', encoding='UTF-8') as f:
                writer = csv.writer(f)
                print("haireta")
                writer.writerow([f'{heartrate}'])
        except :
            sensor_data = "nasi"
            print("you lose")
        





            # # メイン
    def sensor_read():
            global i
            i=3
            print("◆スレッド:", threading.currentThread().getName())
            print('system開始。')
            # スレッドを作る
            
            # スレッドの処理を開始
            thread1 = threading.Thread(target=eye_do)
            thread2 = threading.Thread(target=heartrate)
            

            thread2.start()
            thread1.start()


            # スレッドの処理を待つ
            thread1.join()
            thread2.join()
            i=1+i
            print('system終了。')
            print(f"kigou={kigou}")
            return (left_pupil_x,left_pupil_y,right_pupil_x,right_pupil_y,right_pupil,left_pupil,heart_data)



    left_pupil_x,left_pupil_y,right_pupil_x,right_pupil_y,right_pupil,left_pupil,heart_data = sensor_read() 
    return left_pupil_x,left_pupil_y,right_pupil_x,right_pupil_y,right_pupil,left_pupil,heart_data