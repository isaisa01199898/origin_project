from lib2to3.pygram import pattern_symbols
import dlib
import cv2
import numpy as np
import csv
import tkinter as tk
import datetime

detector = dlib.get_frontal_face_detector()
path = 'C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\shape_predictor_68_face_landmarks.dat'
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

def get_eye_parts(parts, left = True):# 目部分の座標を求める
    if left:
        eye_parts = [
                parts[36],
                min(parts[37],parts[38], key=lambda x: x.y),
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

def get_eye_image(img, parts, left=True):
    if left:
        eyes = get_eye_parts(parts, True)
    else:
        eyes = get_eye_parts(parts, False)

    org_x = eyes[0].x
    org_y = eyes[1].y

    if is_close(org_y, eyes[2].y):
        return None, None

    eye = img[org_y:eyes[2].y, org_x:eyes[-1].x]  # トリミング

    height = eye.shape[0]
    width = eye.shape[1]

    # 👇 ここで拡大する
    resize_eye = cv2.resize(eye, (int(width*20.0), int(height*20.0)))

    # 👇 これを返す（小さいeyeじゃなくて拡大した方）
    return resize_eye, (org_x, org_y)


def draw_points_on_eye_image(eye_img, origin, pupil_loc, eye_center):
    if eye_img is None or origin is None:
        return
    scale = 5
    if pupil_loc:
        rel_x = int((pupil_loc[0] - origin[0]) * scale)
        rel_y = int((pupil_loc[1] - origin[1]) * scale)
        cv2.circle(eye_img, (rel_x, rel_y), 5, (0, 0, 255), -1)  # 赤：瞳孔
    if eye_center:
        rel_x = int((eye_center[0] - origin[0]) * scale)
        rel_y = int((eye_center[1] - origin[1]) * scale)
        cv2.circle(eye_img, (rel_x, rel_y), 5, (0, 255, 255), -1)  # 黄：目の中心

def get_eye_center(img, parts, left = True): #Partsから目のセンター位置を求める
    if left:
        eyes = get_eye_parts(parts, True)
    else:
        eyes = get_eye_parts(parts, False) 

    x_center = int(eyes[0].x + (eyes[-1].x - eyes[0].x)/2)
    y_center = int(eyes[1].y + (eyes[2].y - eyes[1].y)/2)

    cv2.circle(img, (x_center, y_center), 3, (255,255,0), -1)
    return x_center, y_center

def get_pupil_location(img, parts, left = True):#Partsから瞳の位置を求めて表示する
    if left:
        eyes = get_eye_parts(parts, True)
    else:
        eyes = get_eye_parts(parts, False)
    org_x = eyes[0].x
    org_y = eyes[1].y
    if is_close(org_y, eyes[2].y):
        return None
    eye = img[org_y:eyes[2].y, org_x:eyes[-1].x]
    _, threshold_eye = cv2.threshold(cv2.cvtColor(eye, cv2.COLOR_RGB2GRAY),45, 255, cv2.THRESH_BINARY_INV)
     
    center = get_center(threshold_eye)

    if center:
        cv2.circle(img, (center[0] + org_x, center[1] + org_y), 3, (255, 0, 0), -1)
        return center[0] + org_x, center[1] + org_y
    return center

def calculate_relative_pupil_position(img,eye_center, pupil_locate, left = True):
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

def calculate_direction(img, parts, pupil_locate):
    if not pupil_locate:
        return

    eyes = get_eye_parts(parts, True)
    
    left_border = eyes[0].x + (eyes[3].x - eyes[0].x)/3
    right_border = eyes[0].x  + (eyes[3].x - eyes[0].x) * 2/3
    up_border = eyes[1].y + (eyes[2].y - eyes[1].y)/3
    down_border = eyes[1].y + (eyes[2].y - eyes[1].y) * 2/3
    
    if eyes[0].x <= pupil_locate[0] < left_border:
        show_text(img,"LEFT",50,50)
    elif left_border <= pupil_locate[0] <= right_border:
       show_text(img,"STRAIGHT",50,50) 
    elif right_border <= pupil_locate[0] <= eyes[3].x :
        show_text(img,"RIGHT",50,50) 
    else:
        show_text(img,"NONE",50,50) 
    
    if pupil_locate[1] <= up_border:
        show_text(img, "UP", 50, 100)
    elif up_border <= pupil_locate[1] <= down_border:
        show_text(img, "MIDDLE", 50, 100)
    elif pupil_locate[1] >= down_border:
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

def write_csv(data): 
    if not data:
        return
    with open('pupil_locate.csv', 'w', newline='') as f_object:  
        writer_object = csv.writer(f_object)
        writer_object.writerows(data)  
        print("pupil_locate.csvに出力完了")
    return

def append_pupil_locate_to_list(left_pupil_position,right_pupil_position):
    if not left_pupil_position:
        return
    if not right_pupil_position:
        return
    for_write_time = datetime.datetime.now()
    locate = [datetime.date.today(),
              "{}:{}:{}".format(for_write_time.hour, for_write_time.minute, for_write_time.second),
              left_pupil_position[0],left_pupil_position[1],
              right_pupil_position[0],right_pupil_position[1]]
    pupil_locate_list.append(locate)
    return

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read() #Videoを読み込む
    if not ret or frame is None:
        print("カメラから映像を取得できませんでした。")
    frame = cv2.resize(frame, (640, 480))

    frame=frame.astype(np.float32)
    # ここに処理を追加していく　----
    blur = cv2.blur(frame,(31,31))
    blur= blur.astype(np.float32)
    frame = frame*1.0/(blur+1e-6)
    frame = cv2.normalize(frame,None,alpha=0,beta=255,norm_type=cv2.NORM_MINMAX,dtype=cv2.CV_8U)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    dets = detector(frame[:, :, ::-1])

    if len(dets) > 0:

        parts = predictor(frame, dets[0]).parts()
        ret, frame = cap.read()

        left_eye_image, left_origin = get_eye_image(frame, parts, True)
        right_eye_image, right_origin = get_eye_image(frame, parts, False)

        left_eye_center = get_eye_center(frame, parts, True)
        right_eye_center = get_eye_center(frame, parts, False)
        left_pupil_location = get_pupil_location(frame, parts, True)
        right_pupil_location = get_pupil_location(frame, parts, False)

        left_relative_pupil_position = calculate_relative_pupil_position(frame, left_eye_center,left_pupil_location, True)
        right_relative_pupil_position = calculate_relative_pupil_position(frame, right_eye_center,right_pupil_location, False)

        # 👇 追加：拡大画像に点を打つ
        draw_points_on_eye_image(left_eye_image, left_origin, left_pupil_location, left_eye_center)
        draw_points_on_eye_image(right_eye_image, right_origin, right_pupil_location, right_eye_center)

        # 👇 表示
        if left_eye_image is not None:
            cv2.imshow("left", left_eye_image)
        if right_eye_image is not None:
            cv2.imshow("right", right_eye_image)

        calculate_direction(frame,parts,left_pupil_location)
        append_pupil_locate_to_list(left_relative_pupil_position,right_relative_pupil_position)
        cv2.imshow("me", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('e'):
        write_csv(pupil_locate_list)
 
cap.release()
cv2.destroyAllWindows()
