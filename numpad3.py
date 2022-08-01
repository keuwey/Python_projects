import itertools
from collections import defaultdict

letters_by_pad_number = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": ""}

val = 22

message = ""

digits = str(val)
num_group = defaultdict(int)

for digit in digits:
    num_group[digit] += 1

for num in num_group.keys():
    message += letters_by_pad_number[num][num_group[num]-1]

print(message)