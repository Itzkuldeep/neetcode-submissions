class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Self done
        # nums = sorted(nums)
        # res = 0
        # for i in range(len(nums)):
        #     if nums[i] - 1 in nums:
        #         res += 1
        # return res
        # o(nlogn) Bad approach

        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest