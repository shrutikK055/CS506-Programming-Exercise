def addDig(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

num=int(input("Input : "))
result = addDig(num)
print("Output : ", result)
