class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_sum = {}

        for i,num in enumerate(nums):
            if num in prev_sum: return [prev_sum[num],i]
            prev_sum[target-num] = i