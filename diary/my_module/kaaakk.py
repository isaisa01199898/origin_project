import cv2
import numpy as np
import dlib
kigou=""#目線での判定結果
left_pupil_x = None
left_pupil_y = None
right_pupil_x = None
right_pupil_y = None
sensor_data = None

# #ーー変数一覧ーー#

detector = dlib.get_frontal_face_detector()
path = 'C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(path)
pupil_locate_list = [['date','time','right_eye_x','right_eye_y','left_eye_x','left_eye_y']]
gray=0

left_pupil_x, left_pupil_y, right_pupil_x, right_pupil_y = None, None, None, None
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


def get_eye_center(img, parts, left=True):
    try:
        if left:
            eyes = get_eye_parts(parts, True)
        else:
            eyes = get_eye_parts(parts, False)
        x_center = int(eyes[0].x + (eyes[-1].x - eyes[0].x)/2)
        y_center = int(eyes[1].y + (eyes[2].y - eyes[1].y)/2)
        # 座標を必ず表示
        return x_center, y_center
    except Exception as e:
        print(f"get_eye_center error: {e}")
        return None

def get_pupil_location(img, parts, left=True):
    try:
        if left:
            eyes = get_eye_parts(parts, True)
        else:
            eyes = get_eye_parts(parts, False)
        org_x = eyes[0].x
        org_y = eyes[1].y
        if is_close(org_y, eyes[2].y):
            return None
        eye = img[org_y:eyes[2].y, org_x:eyes[-1].x]
        gray = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        _, threshold_eye = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        center = get_center(threshold_eye)
        
        if center:
            px, py = center[0] + org_x, center[1] + org_y
            # 座標を必ず表示
            return px, py
        return None
    except Exception as e:
        print(f"get_pupil_location error: {e}")
        return None

def calculate_relative_pupil_position(img,eye_center, pupil_locate, left = True): #瞳の相対座標を求める
    if not eye_center:
        return
    if not pupil_locate:
        return
    
    relative_pupil_x = pupil_locate[0] - eye_center[0]
    relative_pupil_y = pupil_locate[1] - eye_center[1]

    return relative_pupil_x, relative_pupil_y

def calculate_direction(img, parts, pupil_locate):#瞳の位置と目の座標から瞳が向いている方向を求めて表示する
    if not pupil_locate:
        return

    eyes = get_eye_parts(parts, True)
    
    left_border = eyes[0].x + (eyes[3].x - eyes[0].x)/3 #目を左右に三等分した時の左ゾーンの境目
    right_border = eyes[0].x  + (eyes[3].x - eyes[0].x) * 2/3 #目を左右に三等分した時の右ゾーンの境目
    up_border = eyes[1].y + (eyes[2].y - eyes[1].y)/3 #目を上下に三等分した時の上ゾーンの境目
    down_border = eyes[1].y + (eyes[2].y - eyes[1].y) * 2/3 #目を上下に三等分した時の下ゾーンの境目
    







def append_pupil_locate_to_list(left_pupil_position,right_pupil_position):#現在時刻、右瞳位置、左瞳位置をlistに追加する
    global left_pupil_x, left_pupil_y, right_pupil_x, right_pupil_y

    left_pupil_x =None
    left_pupil_y =None
    right_pupil_x=None
    right_pupil_y=None
    if not left_pupil_position:
        return
    if not right_pupil_position:
        return
    locate = [left_pupil_position[0],left_pupil_position[1],right_pupil_position[0],right_pupil_position[1]]
    
    left_pupil_x = left_pupil_position[0]
    left_pupil_y =left_pupil_position[1]
    right_pupil_x=right_pupil_position[0]
    right_pupil_y=right_pupil_position[1]
    return









left_pupil_x, left_pupil_y, right_pupil_x, right_pupil_y = None, None, None, None
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
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

        left_eye_center = get_eye_center(frame,parts, True)
        right_eye_center = get_eye_center(frame,parts, False)
        left_pupil_location = get_pupil_location(frame, parts, True)
        right_pupil_location = get_pupil_location(frame, parts, False)
        left_relative_pupil_position = calculate_relative_pupil_position(frame, left_eye_center,left_pupil_location, True)
        right_relative_pupil_position = calculate_relative_pupil_position(frame, right_eye_center,right_pupil_location, False)
        calculate_direction(frame,parts,left_pupil_location)
        append_pupil_locate_to_list(left_relative_pupil_position,right_relative_pupil_position)
    cap.release()  # eye_doの最後で呼ぶ



            
