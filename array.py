numbers = [5,9,3,19,70,8,100,2,35,27]
new_array = []
x = 0
while x <= 8:
    new_array.append(numbers[x] * numbers[x + 1])
    x += 1
print(new_array)