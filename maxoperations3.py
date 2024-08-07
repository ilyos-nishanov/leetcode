def maxOperations2(nums,k):
    sums =0
    length = len(nums)
    for i in range(length):
        for j in [nums[j] for j in range(len(nums)) if j!=i]:
            if nums[i]+j ==k:
                sums +=1
                nums.remove(nums[i])
                nums.remove(j)
                length -=2
                break
                
    return sums

print(maxOperations2([3,1,3,4,3],6))