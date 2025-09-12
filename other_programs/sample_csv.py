import os
import cv2  
import datetime

# 仮の瞳座標（本来はGazeTrackingから取得する値）
left_pupil = (123, 456)
right_pupil = (789, 101)

# 現在の時刻を取得
dt_now = datetime.datetime.now()

# 1. ファイル読み込み（あれば）
if os.path.exists('log.txt'):
    with open('log.txt', 'r', encoding='UTF-8') as f:
        print(f.read())

# 2. ログに書き込む（追記）
with open('log.txt', 'a', encoding='UTF-8') as f:
    f.write(f'リアルタイム: {dt_now.strftime("%Y-%m-%d %H:%M:%S")} 左目の座標：{left_pupil} 右目の座標：{right_pupil}\n')
