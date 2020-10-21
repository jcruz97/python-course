import math
countAlpha = len("Hello world")

countFloat = float(countAlpha)

roundPi= round(math.pi,2)

reversedText = "Hello World"[::-1]

age = input("Please write your age : ")
print("You are", age, "years old.", type(age))

num = [2, 8, 1, 4, 6, 3, 7]

sortNum = sorted(num)

sumOfList = sum(num)

minValue = min(num)
maxValue = max(num)

calc = "1 + 2"
stringInterpret = eval(calc)
print(stringInterpret)
