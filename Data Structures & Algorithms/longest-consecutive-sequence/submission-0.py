class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxcons = 0
        for i in nums :
            if not(i-1 in nums) :
                cons = 0
                while (i + cons) in nums :
                    cons += 1
                maxcons = max(cons, maxcons)
        return (maxcons)
        