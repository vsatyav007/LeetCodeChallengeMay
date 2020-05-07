# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Input: [3,2,3]
# Output: 3

# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set1=set(nums)
        for i in set1:
            if nums.count(i)>len(nums)/2:
                return i
