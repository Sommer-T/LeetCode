class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority = len(nums) // 2

        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > majority:
                return n