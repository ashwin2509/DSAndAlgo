class Solution:
    def solution(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1

            if count > max_count:
                max_count = count 

            if nums[i] == 0:
                count = 0

        return count

