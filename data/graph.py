import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
import re
lis = []
left_y_bo=[]
left_y_box = []
left_y= []
right_y_box = []    
right_y = []
right_x= []
left_pupil_x = []   
left_x_box = []
left_box=[]
right_box=[]
left_x = [] 
sensor_box=[]
right_pupil_x = []
time=[]
right_x_box = []
file="C:/Users/isami/OneDrive/Desktop/myproject/data/2025-07-14_22-13-09crearted.csv"
with open(file, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  
    for row in reader:
        del row[:5]
        # print(row)
        time.append([str(value) for value in row if value])  # 数値に変換
time = list(filter(None, time))
realtime = [item for sublist in time for item in sublist]
print(realtime)


with open(file, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        del row[-5:]
        # print(row)
        sensor_box.append([str(value)for value in row if value])  # 数値に変換
sensor_box = list(filter(None, sensor_box))
sensor = [float(item) for sublist in sensor_box for item in sublist]
print(sensor)


max_sensor=(max(sensor))
min_sensor=(min(sensor))
fig, ax = plt.subplots()
ax.set_ylim(min_sensor,max_sensor)

ax.plot( realtime,sensor,'o-')

plt.show()

# with open(file, encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         del row[:2]
#         del row[-3:]
#         print(row)
#         left_y_box.append([str(value) for value in row if value])  # 数値に変換
# left_y_box = list(filter(None, left_y_box))
# # left_y = [float(item) for sublist in left_y_box for item in sublist]

# with open(file, encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         del row[:3]
#         del row[-2:]
#         # print(row)
#         right_x_box.append([str(value) for value in row if value])  # 数値に変換
# right_x_box = list(filter(None, right_x_box))
# # right_x = [float(item) for sublist in right_x_box for item in sublist]


# with open(file, encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         del row[:4]
#         del row[-1:]
#         # print(row)
#         right_y_box.append([str(value) for value in row if value])  # 数値に変換
# right_y_box = list(filter(None, right_y_box))
# # right_y = [float(item) for sublist in right_y_box for item in sublist]

# with open(file, encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         del row[-4:]
#         del row[:1]
#         # print(row)
#         left_x_box.append([str(value)for value in row if value])  # 数値に変換

# left_x_box = list(filter(None, left_x_box))
# # left_x = [float(item) for sublist in left_x_box for item in sublist]
# print(left_x)






# fig, ax = plt.subplots()
# ax.set_ylim(180,430)

# ax.plot( realtime,left_x,'o-',left_y,'o-',right_x,'o-',right_y,'o-')

# plt.show()    
    
                        
                        
# input_csv = pd.read_csv('line.csv')
# first_column_data = input_csv[input_csv.keys()[1]]
# second_column_data = input_csv[input_csv.keys()[2]]

# plt.xlabel(input_csv.keys()[1])
# plt.ylabel(input_csv.keys()[2])

# plt.plot(first_column_data, second_column_data, linestyle='solid', marker='o')
# plt.show()
