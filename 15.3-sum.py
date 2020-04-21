# coding: utf-8

#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.38%)
# Total Accepted:    488.3K
# Total Submissions: 2.1M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# Note:
# The solution set must not contain duplicate triplets.
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            m = len(nums) - 1
            for j in range(i + 1, m):
                if j > i+1 and nums[j] == nums[j -1]:
                    continue
                value = nums[i] + nums[j]
                if value > 0:
                    break
                while m > j:
                    s = value + nums[m]
                    if s < 0:
                        break
                    if s == 0:
                        result.append([nums[i], nums[j], nums[m]])
                        break
                    m = m - 1
        return result
