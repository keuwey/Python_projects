# numbers = [5,9,3,19,70,8,100,2,35,27,33,0,1,21]
# out = [a * b for a, b in zip(numbers, numbers[1:] + [2])]
# print(out)

# numbers = [5,9,3,19,70,8,100,2,35,27,33,0,1,21]
# new_array = []
# x = 0
# while x < len(numbers):
#     nxt = 2 if x+1 >= len(numbers) else numbers[x+1]
#     new_array.append(numbers[x] * nxt)
#     x += 1
# print(new_array)

#function called multiply, taking an int[], returns int[]
def multiply(values):
    newData = []
    valuesLength = len(values) - 1
    for i in range(valuesLength):
        newData.append(values[i] * values[i+1])
    newData.append(values[valuesLength] * 2)
    return newData

#init int[], calling multiply-function and printing the data
numbers = [5,9,3,19,70,8,100,2,35,27,33,0,1,21]
newData = multiply(numbers)
print(newData)