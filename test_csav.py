import re

input_data = open('line.csv', 'r')

num = 1

for row in input_data: if not re.match('#', row): if num % 2 == 0: split_row = row.rstrip('\n').split(',') month = split_row[0] ave_temperature = split_row[1] print(month, ave_temperature) num += 1

input_data.close()

print(month, ave_temperature)