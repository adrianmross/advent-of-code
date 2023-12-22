file = open("1/input.txt", "r")

def getCV(str):
    num = ""
    cv = 0
    for char in str:
        if char.isdigit():
            num += char
    if num != "":
        cv = int(num[0]+num[-1])
    return cv

def solution(file):
    sum = 0
    lines = file.readlines()
    for line in lines:
        sum += getCV(line)
    return sum

print(solution(file))



