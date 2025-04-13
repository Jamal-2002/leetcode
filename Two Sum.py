"""
Two Sum | Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


#Attempt1:

nums = [3,3]
target = 6

for ind, ele in enumerate(nums):
    num1 = ele
    num2 = target - ele
    if num2 in nums[ind+1:]:
        ind1 = ind
        ind2 = nums[ind+1:].index(num2) + ind + 1
        break

        

print(num1, num2)
print(ind1, ind2)



#Attempt2

class Solution(object):
    def twoSum(self, nums, target):
        myMap = {} #value:indice

        for ind, ele in enumerate(nums):
            diff = target - ele
            if diff in myMap:
                return [myMap[diff],ind]
            myMap[ele] = ind
        
