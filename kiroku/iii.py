senosr_data = 80.95 
import numpy
from uuu import dat
r_y,r_x,l_y,l_x= 0, 0, 0, 0
sensor_data = 0.0
def pitagorau(a,b):
    c2=a*a+b*b
    c2=numpy.sqrt(c2)
    return c2
def jude(r_x,r_y,l_x,l_y,sensor_data):
    r_long=pitagorau(r_x,r_y)
    l_long=pitagorau(l_x,l_y)
    dif = r_long - l_long 
    jude_box = ""
    if 80.8 <= sensor_data <= 81.1:                 
        if all(-4 <= v <= 4 for v in [r_y, r_x, l_y, l_x]):
            jude_box = "focus"                      
        elif abs(dif) <= 3:                      
            jude_box = "focus"               
            if abs(l_x)>=5 :                     
                jude_box="focus"                 
                if abs(r_x) >= 7:                
                    jude_box="Nocus"          
                    if abs(r_x)- abs(l_x) <= 4:     
                        jude_box="Nocus"         
    else:
        if  -4 <= r_y and r_x and l_y and l_x <=4 : 
            jude_box = "focus"                      
        elif 5 <= abs(l_x) <= 6:                    
            jude_box="focus"                        
        elif 10 <= abs(l_x) :                       
            jude_box="focus"                        
        else:                                       
            jude_box="Nocus"                     
    return jude_box
while True:
    r_y,r_x,l_y,l_x= None, None, None, None
    sensor_data = None
    while any(v is None for v in [r_x, r_y, l_x, l_y, sensor_data]):
        r_x, r_y, l_x, l_y, sensor_data=dat()
        # print(f"→ dat() = {r_x}, {r_y}, {l_x}, {l_y}, {sensor_data}")


    prom=jude(r_x, r_y, l_x, l_y, sensor_data)
    print(prom)