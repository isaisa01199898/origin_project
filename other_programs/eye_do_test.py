import asyncio
import cv2
import dlib

import datetime
import time
import csv
import pprint
csv_file = 'line.csv'
write_event = asyncio.Event()

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



async def  reader(delay):
    print("")
    await asyncio.sleep(delay)
    if not os.path.exists(csv_file):
        print(f"{csv_file} が存在しません。")
        exit()

    # ファイルサイズが変化するまで待機
    previous_size = os.path.getsize(csv_file)
    print("CSVファイルの書き込みを待機中...")
    while True:
        await write_event.wait()  # データが書き込まれるまで待機
        write_event.clear()  # イベントをリセット
        time.sleep(1)  # 1秒待機
        current_size = os.path.getsize(csv_file)
        if current_size > previous_size:  # サイズが変化した場合
            print("CSVファイルに書き込みが検出されました。")
            break
        else:
            print("CSVファイルのサイズは変化していません。")
            previous_size = current_size
            break
    
    while True:
        i=1
        write_event.clear()  # イベントをリセット
        with open('line.csv', encoding='utf-8') as f:
                        reader = csv.reader(f)
                        rows = list(reader) 
        with open('line.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # ヘッダー行をスキップ
            for left_x in reader:
                del left_x[-6:]
                left_x_box.append([int(value) for value in left_x if value])  # 数値に変換
        
        lis = list(filter(None, left_x_box))
        flat_list_left_x = [item for sublist in left_x_box for item in sublist]
        # print(len(flat_list_left_x))
        if len(flat_list_left_x) > i:
            left_eye_x= [flat_list_left_x[i] - flat_list_left_x[i + 1] for i in range(len(flat_list_left_x) - 1)]
        else:
            print("")
        with open('line.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # ヘッダー行をスキップ
            for left_y in reader:
                del left_y[-5:]
                del left_y[:1]
                left_y_box.append([int(value) for value in left_y if value])  # 数値に変換
        
        
        lis = list(filter(None, left_y_box))
        flat_list_left_y = [item for sublist in left_y_box for item in sublist]
        if len(flat_list_left_y) > i:
            left_eye_y = [flat_list_left_y[j] - flat_list_left_y[j + 1] for j in range(len(flat_list_left_y) - 1)]
        
        with open('line.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # ヘッダー行をスキップ
            for right_x in reader:
                del right_x[-4:]
                del right_x[:2]
                right_x_box.append([int(value) for value in right_x if value])  # 数値に変換
        
        lis = list(filter(None, right_x_box))
        flat_list_right_x = [item for sublist in right_x_box for item in sublist]
        if len(flat_list_right_x) > i:
            right_eye_x = [flat_list_right_x[j] - flat_list_right_x[j + 1] for j in range(len(flat_list_right_x) - 1)]
        
        with open('line.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # ヘッダー行をスキップ
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
        if len(flat_list_right_y) > i:
            # print("seikou")
            right_eye_y= [flat_list_right_y[j] - flat_list_right_y[j + 1] for j in range(len(flat_list_right_y) - 1)]
        else:
            print("")
        # print(f"left_eye_y: {left_eye_y}")
        # print(f"left_eye_x: {left_eye_x}")
        # print(f"right_eye_x: {right_eye_x}")
        # print(f"right_eye_y: {right_eye_y}")
        if left_eye_x and left_eye_y and right_eye_x and right_eye_y is not None:
            if (max(left_eye_y, default=0) > 5 and max(left_eye_x, default=0) > 5 and
                max(right_eye_x, default=0) > 5 and max(right_eye_y, default=0) > 5):
                print("×")
                kigou="batu"
            else:
                print("〇")
                kigou="maru"

async def eye_do(delay):
    print("eye_do_strat")
    await asyncio.sleep(delay)
    class eye_tracking(object):
        print("haireta")
        with open('line.csv', 'w', encoding='UTF-8')as f:
            writer = csv.writer(f)
            print("eye_tracking")
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
    
            
            write_event.set()
            
    
            cv2.imshow("eye", frame)
            
                # Escで終了
            if cv2.waitKey(1) & 0xFF == 27:#escきー
                    break
        
        webcam.release()
        cv2.destroyAllWindows()
    

async def main():
    # doing= asyncio.create_task(reader(0))
    # doing2= asyncio.create_task(eye_do(0))
    await asyncio.gather(
        reader(0),
        eye_do(0)
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())