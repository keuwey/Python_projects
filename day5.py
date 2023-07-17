student_heights = input("Input a list of student heights: ").split()
student_heights = [int(height) for height in student_heights]

count = 0
soma = 0

for x in student_heights:
	soma += x
	count += 1

average_height = soma / count
print(round(average_height))

# student_heights = input("Input a list of student heights: ").split()
# student_heights = [int(height) for height in student_heights]

# average_height = sum(student_heights) / len(student_heights)
# print(round(average_height))
