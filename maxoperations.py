#In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#Return the maximum number of operations you can perform on the array.

# import collections

# def maxOperations3(nums,k):
#     pair = collections.deque(2*[0],2)
#     ans=0
#     for num in nums:
#         pair.appendleft(num)
#         if sum(pair) == k:
#             ans+=1
#     return ans


# print(maxOperations3([3,1,3,4,3],6))


# def maxOperations3(nums,k):
#     leng = len(nums)
#     ans=0
#     for i in range(leng-1):
#         for j in range (leng-1-i):
#             if nums[i]+nums[j]==k:
#                 ans +=1
#                 nums.pop(i)
#                 nums.pop(j)
#     return ans

# print(maxOperations3([3,1,3,4,3],6))



# def maxOperations3(nums,k):
#     ans=0
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)-1):
#             if nums[i]+nums[j]==k:
#                 ans +=1
#                 nums.pop(i)
#                 nums.pop(j)
#     return ans

# print(maxOperations3([3,1,3,4,3],6))


def maxOperations3(nums, k):
    ans = 0
    freq = {}
    
    for num in nums:
        complement = k - num
        if freq.get(complement, 0) > 0:
            ans += 1
            freq[complement] -= 1
        else:
            freq[num] = freq.get(num, 0) + 1
    
    return ans

print(maxOperations3([3,1,3,4,3],6))


def maxOperations3(nums, k):
    from collections import Counter
    
    count = Counter(nums)  # Count occurrences of each number in the list
    ans = 0
    
    for num in count:
        complement = k - num
        if complement in count:
            # For each unique pair (num, complement)
            if complement != num:
                pairs = min(count[num], count[complement])
                ans += pairs
                count[num] -= pairs
                count[complement] -= pairs
            else:
                # If num == complement, count pairs within the same value
                ans += count[num] // 2
                count[num] = 0
    
    return ans

print(maxOperations3([3, 1, 3, 4, 3], 6))
