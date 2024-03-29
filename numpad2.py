import re


def number_to_text(val: str) -> str:
    phone_letters = ["", "", "abc", "def", "ghi",
                     "jkl", "mno", "pqrs", "tuv", "wxyz"]
    groups = [match.group() for match in re.finditer(r'(\d)\1*', val)]
    result = ""
    for group in groups:
        keynumber = int(group[0])
        count = len(group)
        result += phone_letters[keynumber][count - 1]
    return result


decipher_msg = input("Digite os números a serem decifrados: ")
print(number_to_text(decipher_msg))
