
import os
import csv


csv_file = 'C:/Users/isami/OneDrive/Desktop/myproject/data/line.csv'

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




with open(csv_file, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # ヘッダー行をスキップ
    for left_x in reader:
        del left_x[1:]
        del left_x[-2:]

        left_x_box.append([int(value) for value in left_x if value])  # 数値に変換

lis = list(filter(None, left_x_box))
flat_list_left_x = [item for sublist in left_x_box for item in sublist]
print(f"x{flat_list_left_x}")



with open(csv_file, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # ヘッダー行をスキップ
    for left_y in reader:
        del left_y[2:]
        del left_y[-1:]
        left_y_box.append([int(value) for value in left_y if value])  # 数値に変換


lis = list(filter(None, left_y_box))
flat_list_left_y = [item for sublist in left_y_box for item in sublist]


with open(csv_file, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # ヘッダー行をスキップ
    for right_x in reader:
        del right_x[-4:]
        del right_x[:2]
        right_x_box.append([int(value) for value in right_x if value])  # 数値に変換

lis = list(filter(None, right_x_box))
flat_list_right_x = [item for sublist in right_x_box for item in sublist]

with open(csv_file, encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # ヘッダー行をスキップ

    for right_y in reader:
        del right_y[-3:]
        del right_y[:3]

        right_y_box.append([int(value) for value in right_y if value])  # 数値に変換


lis = list(filter(None, right_y_box))
print(lis)
flat_list_right_y = [item for sublist in right_y_box for item in sublist]
print(len(flat_list_right_y))

print(f"left_eye_y: {flat_list_left_y}")
print(f"left_eye_x: {flat_list_left_y}")
print(f"right_eye_x: {flat_list_right_x}")
print(f"right_eye_y: {flat_list_right_y}")


    
    
    
    
    
    
    
    # l_e_x_s_c=len(left_eye_x)
    # # print (l_e_x_s_c)
    # l_e_y_s_c=len(left_eye_y)
    # # print (l_e_y_s_c)
    # r_e_x_s_c=len(right_eye_x)
    # # print (r_e_x_s_c)
    # r_e_y_s_c=len(right_eye_y)
    # # print (r_e_y_s_c)
    
    
    # # print(type(ex_lis))
    
    
    
    # #あまり目線に変化なしのデータ
    
    # left_eye_x_senba = [i for i in left_eye_x if 4 >= i >= -4 ]
    
    # left_eye_y_senba = [i for i in left_eye_y if 4 >= i >= -4 ]
    
    # right_eye_x_senba= [i for i in right_eye_x if 4 >= i >= -4 ]
    
    # right_eye_y_senba= [i for i in right_eye_y if 4 >= i >= -4 ]
    
    # # print (r_e_y_s_c)
    
    
    
    # l_e_x_se=len(left_eye_x_senba)
    
    # # print(l_e_x_se)
    
    # l_e_y_se=len(left_eye_y_senba)
    
    # # print(l_e_y_se)
    
    # r_e_x_se=len(right_eye_x_senba)
    
    # # print(r_e_x_se)
    
    # r_e_y_se=len(right_eye_y_senba)
    
    # # print(r_e_y_se)
    
    # l_e_x_senbatu_par = (l_e_x_se / l_e_x_s_c) *100
    
    # l_e_y_senbatu_par = (l_e_y_se / l_e_y_s_c) *100
    
    # r_e_x_senbatu_par = (r_e_x_se / r_e_x_s_c) *100
    
    # r_e_y_senbatu_par = (r_e_y_se / r_e_y_s_c) *100
    
    
    
    # print(f"{l_e_x_senbatu_par} = ({l_e_x_se} / {l_e_x_s_c}) *100")
    
    # print(f"{l_e_y_senbatu_par} = ({l_e_y_se} / {l_e_y_s_c}) *100")
    
    # print(f"{r_e_x_senbatu_par} = ({r_e_x_se} / {r_e_x_s_c}) *100")
    
    # print(f"{r_e_y_senbatu_par} = ({r_e_y_se} / {r_e_y_s_c}) *100")
    
    
    
    # l_e_x_senbatu_par = int(l_e_x_senbatu_par) 
    
    # l_e_y_senbatu_par = int(l_e_y_senbatu_par) 
    
    # r_e_x_senbatu_par = int(r_e_x_senbatu_par) 
    
    # r_e_y_senbatu_par = int(r_e_y_senbatu_par) 
    
    
    
    # print(f"{l_e_x_senbatu_par}%")
    
    # print(f"{l_e_y_senbatu_par}%")
    
    # print(f"{r_e_x_senbatu_par}%")
    
    # print(f"{r_e_y_senbatu_par}%")
    
    # right_eye_x_abs= list(map(abs,right_eye_x))
    # right_eye_y_abs= list(map(abs,right_eye_y))
    # left_eye_x_abs= list(map(abs, left_eye_x))
    # left_eye_y_abs= list(map(abs, left_eye_y))
    # right_eye_x_ave = sum(right_eye_x_abs) /  len(right_eye_x_abs)
    # right_eye_y_ave = sum(right_eye_y_abs) /  len(right_eye_y_abs)
    # left_eye_x_ave =  sum(left_eye_x_abs) / len(left_eye_x_abs)
    # left_eye_y_ave =  sum(left_eye_y_abs) / len(left_eye_y_abs)
    
    # print(f"{left_eye_y_ave} = {sum(left_eye_y)} /  {len(left_eye_y)}")
    
    # print(type(right_eye_x_abs))
    # print(int(right_eye_x_ave))
    # print(int(right_eye_y_ave))
    # print(int(left_eye_x_ave ))
    # print(int(left_eye_y_ave ))
    
    # big_number_inlist_right_x = [i for i in right_eye_x_abs if i > 22 ]  #22はサンプル閾値 
    # big_number_inlist_right_y = [i for i in right_eye_y_abs if i > 22 ]  #22はサンプル閾値
    # big_number_inlist_left_x = [i for i in left_eye_x_abs if i > 22 ]    #22はサンプル閾値
    # big_number_inlist_left_y = [i for i in left_eye_y_abs if i > 22 ]    #22はサンプル閾値
    
    # print(type(big_number_inlist_right_x))
    # print(type(big_number_inlist_right_y))
    # print(type(big_number_inlist_left_x))
    # print(type(big_number_inlist_left_y))
    
    # print(right_eye_x_abs)
    # print(right_eye_x_abs.index(25))
    # # print(big_number_inlist_right_y)
    # # right_x_henka_number = right_eye_y_abs.index(big_number_inlist_right_y)
    # # print(big_number_inlist_left_x)
    # # right_x_henka_number = left_eye_x_abs.index(big_number_inlist_left_x )
    # # print(big_number_inlist_left_y)
    # # right_x_henka_number = left_eye_y_abs.index(big_number_inlist_left_y )
    
    
    
    
    
    
    # # lis = list((csv.reader(f)))
    # # con = [row for row in lis[:-4]] 
    # # contents = list(filter(None, con))
    # # lis = list(lis)
    # # print(lis)
    # # contents= [row for row in lis[:-4]] 
    # # print(contents)
    # # del contents[:-4]
    # # contents = list(filter(None, contents))
    # # print(contents)
    # # # diffs = [(n[0] - m[0], n[1] - m[1]) for n, m in zip(lis, lis[1:])]
    # # print(diffs)
    
    
    
    
    
    
    # # kyohaheikinnkannseito,
    # # issyuniookiku
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# #おまけ
# # p=['python', 'ruby', 'html', 'javascript', 'script']
# # print(p)
# # ruby =[s for s in p if s != 'ruby']

# # print(ruby)

# # html =[s for s in p if s != 'html']

# # print(html)

# # javasacript =[s for s in p if s != 'javasacript']

# # print(javasacript)

# # script =[s for s in p if s != 'script']

# # print(script)

# #かんすうかできないため、テンプレ化
# # with open('line.csv', encoding='utf-8') as f:
# #   reader = csv.reader(f)
# #     for right in reader:
# #         del right[2:4]
# #         del right[:1]
# #         right_str = ",".join(right)
# #         re.sub("\n", "", right_str)
# #         text=right_str
# #         print(text)
# # with open('line.csv', encoding='utf-8') as f:
# #   reader = csv.reader(f)
# #     for left in reader:
# #         del left[-3:]
# #         print(left)
# #         left_str = ",".join(left)
# #         re.sub("\n", "", left_str)
# #         print(left_str)
# # with open('line.csv', encoding='shift-jis') as f:
# #     lis = (csv.reader(f))
# #     for right in lis:      #houkatuhaatodeeeeeeeeeeeeeeeeee          
# #         del right[2:4]        #houkatuhaatodeeeeeeeeeeeeeeeeee        
# #         del right[:1] 
# #         right=list(right)  
# #         # print("rightislist")
# #         # print(right)
# #         right=[ n - m for n, m in zip(right, right[1:])]
# #         # print("rightisnotlist")
# #         print(right)
#     # for left_x in reader:
        
#         # print(left_x)
#         # del left_x[-5:]
#         # print(left_x)
#         # # left_x=[ n - m for n, m in zip(left_x, left_x[1:])]
#         # # print(left_x)

# # with open('line.csv', encoding='utf-8') as f:
# #     reader = csv.reader(f)
# #     for left_y in reader:
# #         del left_y[-4:]
# #         del left_y[:1]
# #         print(left_y)
# #         # left_y=[ n - m for n, m in zip(left_y, left_y[1:])]
# #         # print(left_y)
        







# #python jude.py
# # zipでする方法
# # lis=[nakami]

# # diffs = [(n[0] - m[0], n[1] - m[1]) for n, m in zip(lis, lis[1:])]
# # print(diffs)