import re
input_data = open('line.csv', 'r')
num = 0
line_b = []
for row in input_data: 
    if not re.match('#', row): 
        if num % 2 == 0: 
            split_row = row.rstrip('\n').split(',') 
            print(split_row)
            line_jude = len(split_row)
            print(type(line_jude))
            print(line_jude)
            line_b.append(line_jude)
            # month = split_row[0] 
            # ave_temperature = split_row[1] 
            # print(month, ave_temperature) 
        num += 1
input_data.close()
print(line_b)
