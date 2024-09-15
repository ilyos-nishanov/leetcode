def findMaxAverage(nums, k):
    nums2 = []
    my_max = -100000
    for my_list in [nums[i:i+k] for i in range(len(nums)-k+1)]:
        cur_max = float(sum(my_list))/float(len(my_list))
        if cur_max > my_max:
            my_max = cur_max
    return my_max

    
print(findMaxAverage([1,12,-5,-6,50,3],4))