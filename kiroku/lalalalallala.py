import matplotlib.pyplot as plt
import csv
from collections import Counter

# CSVファイルの読み込み
with open('C:/Users/isami/OneDrive/Desktop/myproject/kiroku/firstmemoleag.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

# 1列目のデータを1～100行目と101行目以降に分ける
col1_values_1to100 = []
col1_values_101onwards = []

for i, row in enumerate(data):
    try:
        col1_value = float(row[0])  # 1列目の値を取得
    except ValueError:
        continue  # 数値変換できない場合はスキップ

    if i < 100:
        col1_values_1to100.append(col1_value)  # 1〜100行目の値
    else:
        col1_values_101onwards.append(col1_value)  # 101行目以降の値

# 1～100行目と101行目以降の出現回数をカウント
col1_counter_1to100 = Counter(col1_values_1to100)
col1_counter_101onwards = Counter(col1_values_101onwards)

# グラフ描画
plt.figure(figsize=(10, 6))  # グラフのサイズ指定

# 1～100行目の値の出現回数を紫色で描画
plt.bar(col1_counter_1to100.keys(), col1_counter_1to100.values(), color='purple', label='Rows 1-100')

# 101行目以降の値の出現回数を赤色で描画
plt.bar(col1_counter_101onwards.keys(), col1_counter_101onwards.values(), color='red', label='Rows 101-')

# 軸ラベルとタイトル
plt.xlabel('1列目の値')
plt.ylabel('出現回数')
plt.title('1列目の値の出現回数（色分け）')

# 凡例の表示
plt.legend()

# グラフの表示
plt.show()
