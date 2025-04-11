def Rev(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

user_input = input("Input: ")
s = list(user_input) 
Rev(s)
print("Output:", ''.join(s))  