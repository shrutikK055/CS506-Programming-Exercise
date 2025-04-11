def NoOfSteps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num -= 1
        steps += 1
    return steps

# Take input from user
num = int(input("num: "))
result = NoOfSteps(num)
print("Number of steps to reduce to zero:", result)
