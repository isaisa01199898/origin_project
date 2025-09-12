left_eye_x=[51,0,-1,3,2,6,-3,7,10,30,-12,5]
left_eye_y=[0, 4, -2, -12, -6, -32, -10, -12, -2, -30, -33, -47]
right_eye_x=[4, 23, -33, 36, 39, -37, 27, -48, -36, 19, 11, -9]
right_eye_y=[36, 41, 0, 45, -45, 35, 25, 11, -16, -26, 47, -11]

l_e_x_s_c=len(left_eye_x)
print (l_e_x_s_c)
l_e_y_s_c=len(left_eye_y)
print (l_e_y_s_c)
r_e_x_s_c=len(right_eye_x)
print (r_e_x_s_c)
r_e_y_s_c=len(right_eye_y)
print (r_e_y_s_c)


# print(type(ex_lis))
#あまり目線に変化なしのデータ
left_eye_x_senba = [i for i in left_eye_x if 4 >= i >= -4 ]
left_eye_y_senba = [i for i in left_eye_y if 4 >= i >= -4 ]
right_eye_x_senba= [i for i in right_eye_x if 4 >= i >= -4 ]
right_eye_y_senba= [i for i in right_eye_y if 4 >= i >= -4 ]
print (r_e_y_s_c)

l_e_x_se=len(left_eye_x_senba)
print(l_e_x_se)
l_e_y_se=len(left_eye_y_senba)
print(l_e_y_se)
r_e_x_se=len(right_eye_x_senba)
print(r_e_x_se)
r_e_y_se=len(right_eye_y_senba)
print(r_e_y_se)
l_e_x_senbatu_par= (l_e_x_se / l_e_x_s_c) *100
l_e_y_senbatu_par= (l_e_y_se / l_e_y_s_c) *100
r_e_x_senbatu_par= (r_e_x_se / r_e_x_s_c) *100
r_e_y_senbatu_par= (r_e_y_se / r_e_y_s_c) *100

print(int(l_e_x_senbatu_par))
print(int(l_e_y_senbatu_par))
print(int(r_e_x_senbatu_par))
print(int(r_e_y_senbatu_par))


# l_e_x_senbatu_par
# l_e_y_senbatu_par
# r_e_x_senbatu_par
# r_e_y_senbatu_par
# は、それぞれの目のx座標、y座標の変化が少ないデータの割合を表す。＝集中している時が多いか少ないかの割合






