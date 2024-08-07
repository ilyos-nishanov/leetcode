def maxOperations2(nums,k):
    sums =0
    for i in nums:
        for j in [j for j in nums if j!=i]:
            if i+j ==k:
                sums +=1
                nums.remove(i)
                nums.remove(j)
    return sums

print(maxOperations2([3,1,3,4,3],6))