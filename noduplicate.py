def Noduplicate(nums):
    # result = {}
    # for x in nums:
    #     if x not in result:
    #         result[x] = 1
    #     else:
    #         result[x]+=1

    # for x in result:
    #     if result[x] < 2:
    #         return x

    l = 0
    r = len(nums)-1

    while l<r:
        mid = (l+r)//2
        if mid%2 == 1:
            mid -=1
        
        if nums[mid] == nums[mid+1]:
            l = mid +2
        else:
            r = mid
    return nums[l]
        

nums = [3,3,7,7,10,10,11]
print(Noduplicate(nums))
