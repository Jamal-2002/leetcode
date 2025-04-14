"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


Attempt 1 (Failed: Time Limit Exceeded):

class Solution(object):
    def containsDuplicate(self, nums):
        myList = []

        for num in nums:
            if num in myList:
                return True
                break
            myList.append(num)

        return False



Attempt 2 (Failed: Time Limit Exceeded):

class Solution(object):
    def containsDuplicate(self, nums):
        prevContains = {}

        for ind,num in enumerate(nums):
            if num in prevContains.values():
                return True
            else:
                prevContains[ind] = num

        return False


Attempt 3:

class Solution(object):
    def containsDuplicate(self, nums):
        myHashSet = set()

        for num in nums:
            if num in myHashSet:
                return True
    
            myHashSet.add(num)

        return False