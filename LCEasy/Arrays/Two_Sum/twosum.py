"""
Question:

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range(len(nums)):
          if nums[i] + nums[j] == target:
              return[i,j]

      return[]
       
    



""" 
Algorithm:

1) Iterate through the array with two nested loops using indices i and j to check every pair of different elements.
2) If the sum of the pair equals the target, return the indices of the pair.
3) If no such pair is found, return an empty array.
4) There is guaranteed to be exactly one solution, so we will never return an empty array.

"""