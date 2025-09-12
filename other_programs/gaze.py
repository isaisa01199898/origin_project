from lib2to3.pygram import pattern_symbols
import dlib
import cv2

import numpy as np
import csv
import tkinter as tk
import datetime
webcam = cv2.VideoCapture(1,cv2.CAP_DSHOW)
webcam.set(cv2.CAP_PROP_SETTINGS,0)
detector = dlib.get_frontal_face_detector()
path = 'C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\shape_predictor_68_face_landmarks .dat'
predictor = dlib.shape_predictor(path)
pupil_locate_list = [['date','time','right_eye_x','right_eye_y','left_eye_x','left_eye_y']]
gray=0
def no_hahu():
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
        resize_eye = cv2.resize(eye , (int(width*5.0), int(height*5.0)))

        if left : 
            cv2.imshow("left",resize_eye)
            cv2.moveWindow('left', 50, 200)
        else :
            cv2.imshow("right",resize_eye)
            cv2.moveWindow('right', 350, 200)
        
        return eye
# ...existing code...

    def get_eye_center(img, parts, left=True):
        try:
            if left:
                eyes = get_eye_parts(parts, True)
            else:
                eyes = get_eye_parts(parts, False)
            x_center = int(eyes[0].x + (eyes[-1].x - eyes[0].x)/2)
            y_center = int(eyes[1].y + (eyes[2].y - eyes[1].y)/2)
            cv2.circle(img, (x_center, y_center), 3, (255,255,0), -1)
            # 座標を必ず表示
            cv2.putText(img, f"({x_center},{y_center})", (x_center+10, y_center), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)
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
            gray = cv2.cvtColor(eye, cv2.COLOR_RGB2GRAY)
            gray = cv2.GaussianBlur(gray, (5, 5), 0)
            _, threshold_eye = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            center = get_center(threshold_eye)
            
            if center:
                px, py = center[0] + org_x, center[1] + org_y
                cv2.circle(img, (px, py), 3, (255, 0, 0), -1)
                # 座標を必ず表示
                cv2.putText(img, f"({px},{py})", (px+10, py), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)
                return px, py
            return None
        except Exception as e:
            print(f"get_pupil_location error: {e}")
            return None

    def calculate_relative_pupil_position(img,eye_center, pupil_locate, left = True): #目の中心座標と瞳の座標から目の中央に対しての瞳の相対座標を求める
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

        with open('C:\\Users\\isami\\OneDrive\\Desktop\\myproject\\hearate.csv', 'w', newline='') as f_object:  
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
        ret, frame = cap.read() #Videoを読み込む
        if not ret or frame is None:
            print("カメラから映像を取得できませんでした。")
            break
        # ここに処理を追加していく　----
        dets = detector(frame[:, :, ::-1])
        if len(dets) > 0:
            parts = predictor(frame, dets[0]).parts()
            
            left_eye_image =get_eye_image(frame,parts, True)
            right_eye_image = get_eye_image(frame,parts,False)
            left_eye_center = get_eye_center(frame,parts, True)
            right_eye_center = get_eye_center(frame,parts, False)
            left_pupil_location = get_pupil_location(frame, parts, True)
            right_pupil_location = get_pupil_location(frame, parts, False)
            left_relative_pupil_position = calculate_relative_pupil_position(frame, left_eye_center,left_pupil_location, True)
            right_relative_pupil_position = calculate_relative_pupil_position(frame, right_eye_center,right_pupil_location, False)
            calculate_direction(frame,parts,left_pupil_location)
            append_pupil_locate_to_list(left_relative_pupil_position,right_relative_pupil_position)
            write_csv(pupil_locate_list)



            

    cap.release()


def tuyoi():
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks .dat")


    def get_center(gray_img):
        moments = cv2.moments(gray_img, False)
        try:
            return int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])
        except:
            return None


    def is_close(y0, y1):
        if abs(y0 - y1) < 10:
            return True
        return False


    def eye_point(img, parts, left=True):
        if left:
            eyes = [
                    parts[36],
                    min(parts[37], parts[38], key=lambda x: x.y),
                    max(parts[40], parts[41], key=lambda x: x.y),
                    parts[39],
                    ]
        else:
            eyes = [
                    parts[42],
                    min(parts[43], parts[44], key=lambda x: x.y),
                    max(parts[46], parts[47], key=lambda x: x.y),
                    parts[45],
                    ]
        org_x = eyes[0].x
        org_y = eyes[1].y
        if is_close(org_y, eyes[2].y):
            return None

        eye = img[org_y:eyes[2].y, org_x:eyes[-1].x]
        _, eye = cv2.threshold(cv2.cvtColor(eye, cv2.COLOR_RGB2GRAY), 30, 255, cv2.THRESH_BINARY_INV)

        center = get_center(eye)
        if center:
            return center[0] + org_x, center[1] + org_y
        return center


    def p(img, parts, eye):
        if eye[0]:
            cv2.circle(img, eye[0], 3, (255, 255, 0), -1)
        if eye[1]:
            cv2.circle(img, eye[1], 3, (255, 255, 0), -1)

        for i in parts:
            cv2.circle(img, (i.x, i.y), 3, (255, 0, 0), -1)

        cv2.imshow("me", img)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        dets = detector(frame[:, :, ::-1])
        if len(dets) > 0:
            parts = predictor(frame, dets[0]).parts()

            left_eye = eye_point(frame, parts)
            right_eye = eye_point(frame, parts, False)

            p(frame * 0, parts, (left_eye, right_eye))

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
def super():

    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks .dat")
    i = 0

    while i<100:
        _, frame = cap.read()
        
        #グレースケール化
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #ランドマーク
        faces = detector(gray)
        if(len(faces)==0):
            print("顔がカメラに移っていないです。")
        else:
            for face in faces:
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()
                # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

                landmarks = predictor(gray, face)

                # for n in range(0,68):
                #     x = landmarks.part(n).x
                #     y = landmarks.part(n).y
                #     cv2.circle(frame, (x,y), 2, (255,0,0), -1)

            # 瞳のトリミング処理
            # 右目：[36,,37,39, 40]　左目：[42, 43, 45, 46]
            # Right eye
            r_x1,r_y1 = landmarks.part(36).x,landmarks.part(36).y
            r_x2,r_y2 = landmarks.part(37).x,landmarks.part(37).y
            r_x3,r_y3 = landmarks.part(39).x,landmarks.part(39).y
            r_x4,r_y4 = landmarks.part(40).x,landmarks.part(40).y
            # Left eye
            l_x1,l_y1 = landmarks.part(42).x,landmarks.part(42).y
            l_x2,l_y2 = landmarks.part(43).x,landmarks.part(43).y
            l_x3,l_y3 = landmarks.part(45).x,landmarks.part(45).y
            l_x4,l_y4 = landmarks.part(46).x,landmarks.part(46).y

            #　トリミング範囲補正
            trim_val = 2
            r_frame_trim = frame[r_y2-trim_val:r_y4+trim_val, r_x1:r_x3]
            l_frame_trim = frame[l_y2-trim_val:l_y4+trim_val, l_x1:l_x3]

            # 拡大処理（5倍）
            r_height,r_width = r_frame_trim.shape[0],r_frame_trim.shape[1]
            l_height,l_width = l_frame_trim.shape[0],l_frame_trim.shape[1]
            r_frame_trim_resize = cv2.resize(r_frame_trim , (int(r_width*7.0), int(r_height*7.0)))
            l_frame_trim_resize = cv2.resize(l_frame_trim , (int(l_width*7.0), int(l_height*7.0)))

            # グレースケール処理
            r_frame_gray = cv2.cvtColor(r_frame_trim_resize, cv2.COLOR_BGR2GRAY)
            l_frame_gray = cv2.cvtColor(l_frame_trim_resize, cv2.COLOR_BGR2GRAY)

            #平滑化（ぼかし）
            r_frame_gray = cv2.GaussianBlur(r_frame_gray,(7,7),0)
            l_frame_gray = cv2.GaussianBlur(l_frame_gray,(7,7),0)

            # 2値化処理
            thresh = 80
            maxval = 255
            e_th,r_frame_black_white = cv2.threshold(r_frame_gray,thresh,maxval,cv2.THRESH_BINARY_INV)
            l_th,l_frame_black_white = cv2.threshold(l_frame_gray,thresh,maxval,cv2.THRESH_BINARY_INV)

                        #輪郭の表示
            # OpenCV 4系以降はこちら
            r_eye_contours, hierarchy = cv2.findContours(r_frame_black_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            r_eye_contours = sorted(r_eye_contours, key=lambda x: cv2.contourArea(x), reverse=True)


            if(len(r_eye_contours)==0):
                print("Right Blink")
            else:
                for cnt in r_eye_contours:
                    (x, y, w, h) = cv2.boundingRect(cnt)
                    # cv2.drawContours(r_frame_trim_resize, [cnt], -1, (0,0,255),3) #輪郭の表示
                    # cv2.rectangle(r_frame_trim_resize, (x, y), ((x + w, y + h)), (255, 0, 0), 2)#矩形で表示
                    cv2.circle(r_frame_trim_resize, (int(x+w/2), int(y+h/2)), int((w+h)/4), (255, 0, 0), 2) #円で表示
                    cv2.circle(frame, (int(r_x1+(x+w)/10), int(r_y2-3+(y+h)/10)), int((w+h)/20), (0, 255, 0), 1)    #元画像に表示
                    break

                l_eye_contours, hierarchy_l = cv2.findContours(l_frame_black_white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                l_eye_contours = sorted(l_eye_contours, key=lambda x: cv2.contourArea(x), reverse=True)
            if(len(l_eye_contours)==0):
                print("Left Blink")
            else:
                for cnt in l_eye_contours:
                    (x, y, w, h) = cv2.boundingRect(cnt)
                    # cv2.drawContours(l_frame_trim_resize, [cnt], -1, (0,0,255),3) #輪郭の表示
                    # cv2.rectangle(l_frame_trim_resize, (x, y), ((x + w, y + h)), (255, 0, 0), 2)#矩形で表示
                    cv2.circle(l_frame_trim_resize, (int(x+w/2), int(y+h/2)), int((w+h)/4), (255, 0, 0), 2) #円で表示
                    cv2.circle(frame, (int(l_x1+(x+w)/10), int(l_y2-3+(y+h)/10)), int((w+h)/20), (0, 255, 0), 1)    #元画像に表示
                    break


            #画像の表示    
            cv2.imshow("frame",frame)
            
            cv2.imshow("right eye trim",r_frame_trim_resize)
            cv2.imshow("left eye trim",l_frame_trim_resize)

            cv2.imshow("right eye black white",r_frame_black_white)
            cv2.imshow("left eye black white",l_frame_black_white)

            #ウィンドウの配置変更
            cv2.moveWindow('frame', 200,0)
            cv2.moveWindow('right eye trim', 100,100)
            cv2.moveWindow('left eye trim', 240,100)
            cv2.moveWindow('right eye black white', 100,250)
            cv2.moveWindow('left eye black white', 240,250)



    cv2.destroyAllWindows()

def eye_do():
    global webcam
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("未接続")
        return

    gaze = GazeTracking()
    count = 0

    while True:
        ret, frame = webcam.read()
        if not ret or frame is None:
            print("カメラからフレームが取得できませんでした")
            break

        gaze.refresh(frame)
        frame = gaze.annotated_frame()

        # ここで瞳情報などを取得
        left_pupil_x = gaze.pupil_left_coords_x()
        left_pupil_y = gaze.pupil_left_coords_y()
        right_pupil_x = gaze.pupil_right_coords_x()
        right_pupil_y = gaze.pupil_right_coords_y()

        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)
        if key == 27:  # ESCキーで終了
            break

    webcam.release()
    cv2.destroyAllWindows()


no_hahu()
#yosikawa