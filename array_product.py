'''
Given an integer array nums, return an array answer such 
that answer[i] is equal to the product of all the elements 
of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and 
without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
def productExceptSelf(nums:list):
#     answer = []
#     for i in range(len(nums)):
#         product = 1
#         temp = nums[:i]+nums[i+1:]
#         for i in temp:
#             product *= i
#         answer.append(product)
#     return answer


    left_product = 1
    right_product = 1
    n=len(nums)
    answer = [1]*n
    for i in range(n):
        answer[i] *=left_product
        left_product *= nums[i]
    for i in range(n-1,-1,-1):
        answer[i]*=right_product
        right_product*=nums[i]
        
    return answer

print(productExceptSelf([1,2,3,4,5]))