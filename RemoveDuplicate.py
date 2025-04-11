def Dup(nums):
    if not nums:
        return 0
    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1
    return index

# Example 1
nums = [1, 1,  2]
length = Dup(nums)
print(length)      
print(nums[:length])  


# Example 2
nums = [0, 0, 1, 1,  1, 2,  2, 3, 3, 4]
length = Dup(nums)
print(length)      
print(nums[:length])  
