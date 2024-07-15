def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False

print(increasingTriplet([5,3,2,1,0]))