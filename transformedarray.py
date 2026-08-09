nums = [-1,4,-1]
result = [0]*len(nums)
for i in range(len(nums)):
    if nums[i] > 0:
        temp = (i+nums[i]) % len(nums)
        result[i] = nums[temp]
    elif nums[i] < 0:
        temp = (i-abs(nums[i])) % len(nums)
        result[i] = nums[temp]
    else:
        result[i] = nums[i]


print(result)