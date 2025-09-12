import cv2
import dlib
from gaze_tracking.gaze_tracking import GazeTracking
import os
import datetime
import csv
import pprint
import os
import cv2  
import datetime
import gaze_tracking.gaze_tracking as gt
text=None
left_x_box=[]
left_y_box=[]
right_x_box=[]
right_y_box=[]
left_eye_x=[]
left_eye_y=[]
right_eye_x=[]
right_eye_y=[]
flat_list_left_x=[]
flat_list_left_y=[]
flat_list_right_x=[]
flat_list_right_y=[]
i=40
kigou=str()
count=0
kigou="wahhaha"
class eye_tracking(object):
    with open('line.csv', 'w', encoding='UTF-8')as f:
        writer = csv.writer(f)
        writer.writerow(['左目のx座標','左目のy座標','右目のx座標','右目のy座標','方向','右目の座標','左目の座標'])
    
    print(gt.__file__)
    print(">>> loading GazeTracking from:", gt.__file__)
    print(">>> available methods:", [m for m in dir(gt.GazeTracking) if not m.startswith("_")])
    
    
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("未接続")
        exit()
    
    while True:
        i = 0
        _, frame = webcam.read()
        # print(frame.shape, frame.dtype)
        # 確認
        gaze.refresh(frame)
        
        # print("frame before refresh:", frame.shape, frame.dtype)
    
        # 顔＋瞳に十字線を描画した結果を取得
        frame = gaze.annotated_frame()
    
        text = " "


        # 0→瞬き　1→真ん中　2→右　3→左
        text = ""
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

        cv2.putText(frame, text, (90, 60),
                    cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    
        # 瞳の座標を描画
        count+=1
        left_pupil_x = gaze.pupil_left_coords_x()
        left_pupil_y = gaze.pupil_left_coords_y()
        left_pupil = left_pupil_x,left_pupil_y
        right_pupil_x = gaze.pupil_right_coords_x()
        right_pupil_y = gaze.pupil_right_coords_y()
        right_pupil = right_pupil_x,right_pupil_y
        if left_pupil_x is not None and right_pupil_x is not None and left_pupil_y is not None and right_pupil_y is not None:
            with open('line.csv', 'a', encoding='UTF-8') as f:
                writer = csv.writer(f)
                writer.writerow([f'{left_pupil_x}',f'{left_pupil_y}', f'{right_pupil_x}',f'{right_pupil_y}',f'{text}',f'{right_pupil}',f'{left_pupil}'])
        
            cv2.putText(frame, "Left pupil:  " + str(f"{left_pupil_x},{left_pupil_y}"),
                        (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
            cv2.putText(frame, "Right pupil: " + str(f"{right_pupil_x},{right_pupil_y}"),
                        (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
            cv2.putText(frame,"kigou:"+ str(f"{kigou}"), (90, 195),
                        cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        # print(f"{text}")
        now = datetime.datetime.now()

        


        cv2.imshow("eye", frame)
        
            # Escで終了
        if cv2.waitKey(1) & 0xFF == 27:#escきー
                break
    
    webcam.release()
    cv2.destroyAllWindows()
    
#python eye_do.py
#settingの方法
#bodyは必ず平行に
#一番目のせきの左側（一番）
#ｐｃ左は85度
#