def rotate(nums,k):
    cnt = 0
    while cnt<k:
        last = nums[len(nums)-1]
        for i in range(len(nums)-1,0,-1):

            nums[i] = nums[i-1]
        cnt +=1
        
        nums[0] = last
    
nums = [-1]
# print(nums)
# rotate(nums,3)
# print(nums)

def reverse_nums(nums,i,j):
    while i < j:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j-=1
reverse_nums(nums,0,len(nums)-1)
reverse_nums(nums,0,2)
reverse_nums(nums,3,len(nums)-1)
print(nums)