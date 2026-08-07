nums = [5,4,0,3,1,6,2]
max_len = 0
for i in range(len(nums)):
    result = []
    flag = 1
    while flag:
        temp = nums[i]
        if temp not in result:
            result.append(temp)
            i = temp
        else:
            flag = 0

    max_len = max(max_len,len(result))
print(max_len)