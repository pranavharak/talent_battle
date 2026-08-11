
# def special(nums):
#     if len(nums)==1:
#         return True
#     for i in range(len(nums)-1):
#         if nums[i]%2 == nums[i]%2:
#             return False
#     return True

# nums = [4,3,1,6]
# print(special(nums))

def special2(nums,queries):
    result =[]
    for i in range(len(queries)):
        temp = True
        for j in range(queries[i][0],queries[i][1]):
            
            if nums[j]%2 == nums[j+1] %2:
                temp = False 
                break  
        result.append(temp)
    return result

nums = [4,3,1,6]
queries = [[0,2],[2,3]]
print(special2(nums,queries))