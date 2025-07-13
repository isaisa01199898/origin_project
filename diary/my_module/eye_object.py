import cv2
import re
from ..gaze_tracking import GazeTracking
import threading
import datetime
import serial
import csv
sensor_data=0
i=3
kigou=""#目線での判定結果
# #ーー変数一覧ーー#

def data_get():
    global left_pupil,right_pupil_x,right_pupil_y,left_pupil_x,left_pupil_y,left_pupil,heart_data

    def eye_do():
            global s
            global left_pupil_x, left_pupil_y, right_pupil_x, right_pupil_y, right_pupil, left_pupil, heart_data
            global s, b, count  # ←ここにcountを追加

            left_pupil_x = None
            left_pupil_y = None
            count=0

            right_pupil_x = None
            right_pupil_y = None
            text = None
            left_pupil = None
            right_pupil = None
            global b
            
                # class eye_tracking(object):
                #     print("haireta")
                #     # with open('line.csv', 'w', encoding='UTF-8')as f:
                #     #     writer = csv.writer(f)
                #     #     print("eye_tracking")
                #     #     writer.writerow(['左目のx座標','左目のy座標','右目のx座標','右目のy座標','方向','右目の座標','左目の座標'])
                    
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
            if left_pupil_x is not None and right_pupil_x is not None and left_pupil_y is not None and right_pupil_y is not None  :
                print("")
            else:
                print("mouikkai")







    def heartrate():
        global i
        global sensor_data
        ser = serial.Serial('com3',9600)
        data = []
        i=i+1
        while len(data) < i:     #forではできない
            line = ser.readline().strip()
            data.append(line)
            
        ser.close()

        sensor_data = float(data[-1])
        print(f"{sensor_data}")






    # # メイン

    while True:
        print("◆スレッド:", threading.currentThread().getName())
        # スレッドを作る
        
        # スレッドの処理を開始
        thread1 = threading.Thread(target=eye_do)
        thread2 = threading.Thread(target=heartrate)
        

        thread2.start()
        thread1.start()


        # スレッドの処理を待つ
        thread1.join()
        thread2.join()
        with open('line.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            time_now = datetime.datetime.now()
            writer.writerow([f'{sensor_data}',f'{left_pupil_x}', f'{left_pupil_y}',f'{left_pupil}',f'{right_pupil_x}',f'{right_pupil_y}',f"{right_pupil}",f'{time_now}'])
            return sensor_data,left_pupil_x,left_pupil_y,left_pupil,right_pupil_x,right_pupil_y,right_pupil,time_now



    