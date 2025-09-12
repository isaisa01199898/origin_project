import matplotlib.pyplot as plt
import japanize_matplotlib

# data = [76.63,
# 81.08,
# 81.08,
# 81.19,
# 81.08,
# 80.97,
# 81.19,
# 81.08,
# 80.97,
# 81.19,
# 81.08,
# 80.97,
# 81.3,
# 81.08,
# 80.97,
# 81.19,
# 81.08,
# 80.97,
# 81.19,
# 81.08,
# 80.97,
# 81.3,
# 81.08,
# 80.86,
# 81.3,
# 80.97,
# 81.19]


#l_x
data=[-6,             
4,             
7,             
2,             
5,             
4,             
-3,             
2,             
0,             
-4,             
-1,             
2,             
2,             
1,             
-5,             
2,             
-4,             
11,             
3,             
-7,             
-3,             
-1,             
-1,             
-1,             
1,             
-1]
#r_y
data=[0,
11,
10,
-1,
-1,
4,
1,
9,
9,
9,
2,
13,
12,
0,
0,
1,-
0,
5,
0,
0,
6,
-1,
-1,
-1,
-1,
-1,
-1,]
#r_y
data=[0,
1,
0,
0,
0,
0,
-1,
2,
2,
2,
-1,
0,
0,
0,
-1,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,]

#l_y
data=[0,
-1,
-1,
-1,
0,
-1
-2,
1,
0,
-2,
-2,
0,
-1,
-1,
0,
-2,
-2,
0,
-1,
-2,
-3,
-2,
-2,
-2,
2,
-2,
-2,]
interval = 1  # 秒間隔

# 2の倍数行の行番号
rows_2 = [i for i in range(2, len(data)+1) if i % 2 == 0]
results_2 = [data[i-1] - data[i-2] for i in rows_2]

# 行番号を秒に変換
times_sec = [(r-1) * interval for r in rows_2]

# 表示範囲（秒換算）
start_sec = 0  # 2分50秒
end_sec   = 25  # 3分17秒

# フィルタ
filtered_times = [t for t in times_sec if start_sec <= t <= end_sec]
filtered_results = [val for t, val in zip(times_sec, results_2) if start_sec <= t <= end_sec]

# 秒 → 分:秒の文字列に変換（x軸ラベル用）
time_labels = [f"{t//60}:{t%60:02d}" for t in filtered_times]
print(filtered_results)
# グラフ描画
plt.figure(figsize=(8,4))
plt.plot(time_labels, filtered_results, marker='o', color='orange')
plt.title("2の倍数行の値 - 1行前の値（2:50〜3:17）")
plt.xlabel("時間")
plt.ylabel("差の値")
plt.grid(True)
plt.show()
