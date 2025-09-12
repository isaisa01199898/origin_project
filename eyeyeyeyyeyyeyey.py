from lib2to3.pygram import pattern_symbols
import dlib
import cv2
import numpy as np
import csv
import tkinter as tk
import datetime
left_eye=None
right_eye=None
detector = dlib.get_frontal_face_detector()
path = "C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(path)
pupil_locate_list = [['date','time','right_eye_x','right_eye_y','left_eye_x','left_eye_y']]

def is_close(y0,y1): #目が閉じているか判定する関数
    if abs(y0 - y1) < 10:
        return True
    return False

def get_center(gray_img):#二値化された目画像から瞳の重心を求める
    moments = cv2.moments(gray_img, False)
    try:
        
        return int(moments['m10']/moments['m00']), int(moments['m01'] / moments['m00'])
    except:
        return None

def p(img, parts, eye):
    if eye[0]:
        cv2.circle(img, eye[0], 3, (255,255,0), -1)
    if eye[1]:
        cv2.circle(img, eye[1], 3, (255,255,0), -1)  
    for i in parts:
        cv2.circle(img, (i.x, i.y), 3, (255, 0, 0), -1)

    cv2.imshow("me", img)  

def get_eye_parts(parts, left = True):# 目部分の座標を求める
    if left:
        eye_parts = [
                parts[36],
                min(parts[37],parts[38], key=lambda x: x.y),#parts[37].yとparts[38].yの大きいほう
                max(parts[40],parts[41], key=lambda x: x.y),
                parts[39],
            ]
    else:
        eye_parts = [
                parts[42],
                min(parts[43],parts[44], key = lambda x: x.y),
                max(parts[46],parts[47], key=lambda x: x.y),
                parts[45],
            ]
    return eye_parts



def get_eye_image(img, parts, left = True): #カメラ画像と見つけた顔の座標から目の画像を求めて表示する
    if left:
        eyes = get_eye_parts(parts, True)
    else:
        eyes = get_eye_parts(parts, False)
    org_x = eyes[0].x
    org_y = eyes[1].y

    if is_close(org_y, eyes[2].y):
        return None
    eye = img[org_y:eyes[2].y, org_x:eyes[-1].x] #画像から瞳部分をトリミング　
    # img[top : bottom, left : right]
    # Pythonのリスト：マイナスのインデックスは最後尾からの順番を意味する  

    height = eye.shape[0]
    width = eye.shape[1]
    resize_eye = cv2.resize(eye , (int(width*40.0), int(height*40.0)))

    if left : 
        cv2.imshow("left",resize_eye)
        cv2.moveWindow('left', 50, 200)
    else :
        cv2.imshow("right",resize_eye)
        cv2.moveWindow('right', 350, 200)
    
    return eye

def get_eye_center(img, parts, left = True): #Partsから目のセンター位置を求めて、表示する
        if left:
            eyes = get_eye_parts(parts, True)
        else:
            eyes = get_eye_parts(parts, False) 

        x_center = int(eyes[0].x + (eyes[-1].x - eyes[0].x)/2)
        y_center = int(eyes[1].y + (eyes[2].y - eyes[1].y)/2)

        cv2.circle(img, (x_center, y_center), 3, (255,255,0), -1)
        return x_center, y_center

def get_pupil_location(img, parts, left = True):#Partsから瞳の位置を求めて表示する、その過程で目の二値化画像を表示
    if left:
            eyes = get_eye_parts(parts, True)
    else:
            eyes = get_eye_parts(parts, False)
    org_x = eyes[0].x
    org_y = eyes[1].y
    if is_close(org_y, eyes[2].y):
        return None
    eye = img[org_y:eyes[2].y, org_x:eyes[-1].x]
    _, threshold_eye = cv2.threshold(cv2.cvtColor(eye, cv2.COLOR_RGB2GRAY),45, 255, cv2.THRESH_BINARY_INV)#第一引数を無視して二値化
    
    height = threshold_eye.shape[0]
    width = threshold_eye.shape[1]
    resize_eye = cv2.resize(threshold_eye , (int(width*5.0), int(height*5.0)))

    if left : 
        cv2.imshow("left_threshold",resize_eye)
        cv2.moveWindow('left_threshold', 50, 300)
    else :
        cv2.imshow("right_threshold",resize_eye)
        cv2.moveWindow('right_threshold', 350, 300)
    
    center = get_center(threshold_eye)

    if center:
        cv2.circle(img, (center[0] + org_x, center[1] + org_y), 3, (255, 0, 0), -1)
        return center[0] + org_x, center[1] + org_y
    return center

def calculate_relative_pupil_position(img,eye_center, pupil_locate, left = True): #目の中心座標と瞳の座標から目の中央に対しての瞳の相対座標を求める
    if not eye_center:
        return
    if not pupil_locate:
        return
    
    relative_pupil_x = pupil_locate[0] - eye_center[0]
    relative_pupil_y = pupil_locate[1] - eye_center[1]
    if left:
        cv2.putText(img,
            "left x=" + str(relative_pupil_x) + " y=" + str(relative_pupil_y),
            org=(50, 400),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_4)

    else:
        cv2.putText(img,
            "right x=" + str(relative_pupil_x) + " y=" + str(relative_pupil_y),
            org=(50, 450),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_4)
    
    return relative_pupil_x, relative_pupil_y

def calculate_direction(img, parts, pupil_locate):#瞳の位置と目の座標から瞳が向いている方向を求めて表示する
    if not pupil_locate:
        return

    eyes = get_eye_parts(parts, True)
    
    left_border = eyes[0].x + (eyes[3].x - eyes[0].x)/3 #目を左右に三等分した時の左ゾーンの境目
    right_border = eyes[0].x  + (eyes[3].x - eyes[0].x) * 2/3 #目を左右に三等分した時の右ゾーンの境目
    up_border = eyes[1].y + (eyes[2].y - eyes[1].y)/3 #目を上下に三等分した時の上ゾーンの境目
    down_border = eyes[1].y + (eyes[2].y - eyes[1].y) * 2/3 #目を上下に三等分した時の下ゾーンの境目
    
    if eyes[0].x <= pupil_locate[0] < left_border:
        #瞳は左側にある
        show_text(img,"LEFT",50,50)
    elif left_border <= pupil_locate[0] <= right_border:
        #瞳は真ん中にある
        show_text(img,"STRAIGHT",50,50) 
    elif right_border <= pupil_locate[0] <= eyes[3].x :
        show_text(img,"RIGHT",50,50) 
    else:
        #瞳はどこにもない
        show_text(img,"NONE",50,50) 
    
    if pupil_locate[1] <= up_border:
        #瞳は上にある
        show_text(img, "UP", 50, 100)
    elif up_border <= pupil_locate[1] <= down_border:
        #瞳は中位置にある
        show_text(img, "MIDDLE", 50, 100)
    elif pupil_locate[1] >= down_border:
        #瞳は下位置にある
        show_text(img, "DOWN", 50, 100)
    return


def show_text(img, text, x, y):
    cv2.putText(img,
            text,
            org=(x, y),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_4)
    return



def write_csv(data): #listを受け取ってpupil_locate.csvに吐く
    if not data:
        return

    with open('pupil_locate.csv', 'w', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = csv.writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerows(data)  
        # Close the file object
        print("pupil_locate.csvに出力完了")
    return

def append_pupil_locate_to_list(left_pupil_position,right_pupil_position):#現在時刻、右瞳位置、左瞳位置をlistに追加する
    if not left_pupil_position:
        return
    if not right_pupil_position:
        return
    for_write_time = datetime.datetime.now()
    locate = [datetime.date.today(), "{}:{}:{}".format(for_write_time.hour, for_write_time.minute, for_write_time.second),left_pupil_position[0],left_pupil_position[1],right_pupil_position[0],right_pupil_position[1]]
    pupil_locate_list.append(locate)

    return






cap = cv2.VideoCapture(0)


while True:
    left_pupil_x, left_pupil_y, right_pupil_x, right_pupil_y = None, None, None, None
    ret, frame = cap.read()
    
    if not ret or frame is None:
        print("カメラから映像を取得できませんでした。")
        continue  # カメラ取得失敗時はスキップ
    dets = detector(frame[:, :, ::-1])

    if len(dets) > 0:
        parts = predictor(frame, dets[0]).parts()
        
        left_eye_image = get_eye_image(frame, parts, True)
        right_eye_image = get_eye_image(frame, parts, False)
        left_eye_center = get_eye_center(frame, parts, True)
        right_eye_center = get_eye_center(frame, parts, False)
        left_pupil_location = get_pupil_location(frame, parts, True)
        right_pupil_location = get_pupil_location(frame, parts, False)
        left_relative_pupil_position = calculate_relative_pupil_position(frame, left_eye_center,left_pupil_location, True)
        right_relative_pupil_position = calculate_relative_pupil_position(frame, right_eye_center,right_pupil_location, False)
        calculate_direction(frame, parts, left_pupil_location)
        append_pupil_locate_to_list(left_relative_pupil_position,right_relative_pupil_position)

        # 👇ここで目のフレームに点を描画
        for i in get_eye_parts(parts, True):  # 左目
            cv2.circle(frame, (i.x, i.y), 2, (0, 0, 255), -1)
        for i in get_eye_parts(parts, False): # 右目
            cv2.circle(frame, (i.x, i.y), 2, (0, 0, 255), -1)

    cv2.imshow("me", frame)


    key = cv2.waitKey(1) # 1ミリ秒キー入力を待つ

    if key == 27: #Windowを選択された状態でESCボタンを押されたら
        break
    elif key == ord('e'):#Eキーが押されたら
        write_csv(pupil_locate_list)

cap.release()
cv2.destroyAllWindows()