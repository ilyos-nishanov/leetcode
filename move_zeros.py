def moveZeroes(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)
    return nums

print(moveZeroes([2,3,5,0,4,0,2,5,0,1]))