input_list = [1, 2, 3, 4, 5, 99]

target = 5

for index, value in enumerate(input_list):
    if value == target:
        break
else:
    index = -1

print('index:', index)
