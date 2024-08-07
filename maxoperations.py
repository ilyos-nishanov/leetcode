def maxOperations(nums,k):
    left = 0
    right = len(nums)-1
    ans = 0
    while left<right:

        if nums[left]+nums[right] == k:
            ans +=1
        left +=1
        right -=1
    return ans

print(maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4],5))