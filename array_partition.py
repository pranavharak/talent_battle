# not optimal 
nums = [6,2,6,5,1,2]
nums.sort()
result = []
for i in range(len(nums)):
    
    for j in range(i+1,len(nums)):
        temp = []
        temp.append(nums[i])
        temp.append(nums[j])
        if temp not in result:
            result.append(temp)
print(result)
left = 0
right = len(result)-1
max_sum = 0
while left<=right:
    m_sum = min(result[left]) + min(result[right])
    print(f"{min(result[left])} + {min(result[right])}")
    max_sum = max(max_sum,m_sum)
    left +=1
    right -=1
print(max_sum)