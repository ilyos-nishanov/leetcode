
def findMaxAverage(nums, k):

    start = 0
    end = k
    average = 0.0
    
    # Calculate the average of the first window
    for i in range(k):
        average += float(nums[i]) / k
    
    # Initialize the maximum average
    max_average = average
    
    # Slide the window and update the maximum average
    while end < len(nums):
        average -= float(nums[start]) / k
        average += float(nums[end]) / k
        max_average = max(max_average, average)
        start += 1
        end += 1
    
    return max_average

print(findMaxAverage([1,12,-5,-6,50,3],4))
