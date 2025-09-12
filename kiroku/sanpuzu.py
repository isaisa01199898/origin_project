import matplotlib.pyplot as plt
import csv

plt.ion()

# CSV読み込み
with open('C:/Users/isami/OneDrive/Desktop/myproject/kiroku/firstmemoleag.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

# データ分ける
x1, y1 = [], []  # 1〜100行目（青）
x2, y2 = [], []  # 101行目以降（赤）

for i, row in enumerate(data):
    try:
        y_val = float(row[0])
        x_val = float(row[4])
        #0→hr
        #1→l_x
        #2→l_y
        #3→r_x
        #4→r_y
        
    except ValueError:
        # 数値変換できないデータはスキップ（例：ヘッダーとか）
        continue

    if i < 100:
        y1.append(y_val)
        x1.append(x_val)
    else:
        y2.append(y_val)
        x2.append(x_val)
import os
import pandas as pd

folder_path = 'C:/Users/isami/OneDrive/Desktop/myproject/kiroku'
nomal="80.35"
results = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        col0 = pd.to_numeric(df.iloc[:, 0], errors='coerce')
        mean_heart_rate = col0.dropna().mean()

        results.append(mean_heart_rate)

# 全ファイルの平均の平均を計算（NoneやNaNを除外）
overall_mean = pd.Series(results).dropna().mean()

print(f'全ファイルの心拍数平均の平均値: {overall_mean}')
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'MS Gothic'


# CSV読み込み
df = pd.read_csv("C:/Users/isami/OneDrive/Desktop/myproject/kiroku/firstmemoleag.csv", header=None)
heart_rate = pd.to_numeric(df.iloc[:, 0], errors='coerce')
baseline = 80.35
df['差分'] = heart_rate - baseline

# 前半と後半に分割し、差分を丸める（小数第2位）
early_diff = df['差分'][:100].round(2)
late_diff = df['差分'][100:].round(2)

# 頻度をカウント
early_counts = early_diff.value_counts().sort_index()
late_counts = late_diff.value_counts().sort_index()

# x軸の差分値をすべて取得（unionで統合）
all_diff_values = sorted(set(early_counts.index).union(set(late_counts.index)))

# 散布図プロット用に y（回数）を取得（出てこない値は 0 にする）
early_y = [early_counts.get(x, 0) for x in all_diff_values]
late_y = [late_counts.get(x, 0) for x in all_diff_values]

# 散布図描画
plt.figure(figsize=(14,6))

early_nonzero = early_counts[early_counts > 0]
late_nonzero = late_counts[late_counts > 0]
print(early_nonzero)
print(late_nonzero)
# 散布図描画
print(len(x1))
print(len(early_nonzero.index))
plt.scatter(x1, early_diff, color='blue', marker='o', label='focus')

plt.xlabel('gaze(r_y)')
plt.ylabel('heart')
plt.legend()
plt.title('Focus plott')
plt.show()
plt.pause(10)
