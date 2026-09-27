class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # storage = 0
        # for i in range(len(heights)):
        #     for j in range(len(heights)-1, i, -1):
        #         w = j - i
        #         h = min(heights[i], heights[j])
        #         count = w * h
        #         storage = max(storage, count)
        # return storage

        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return res