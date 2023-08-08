student_scores = input("Input a list of student scores ").split()
student_scores = [int(score) for score in student_scores]
max_value = 0
for score in student_scores:
    if score > max_value:
        max_value = score
print("The highest score in the class is: %d" % max_value)
