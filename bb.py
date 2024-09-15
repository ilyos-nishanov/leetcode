def findMaxAverage(nums, k):
    start = 0
    end = k
    
    average = sum(nums[start:end])/k
    max_average = average

    while end<len(nums):
        average -= float(nums[start])/k
        average += float(nums[end])/k
        start +=1
        end +=1
        max_average = max(average, max_average)
    return max_average

print(findMaxAverage([1,12,-5,-6,50,3],4))