''' Hard
https://leetcode.com/problems/trapping-rain-water/
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # Find trapped waters, going from left to right
        trapped_water = 0
        l, r = 0, len(height)-1
        max_left, max_right = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < max_left:
                    trapped_water += (max_left - height[l])
                else:
                    max_left = height[l]
                l += 1
            else:
                if height[r] < max_right:
                    trapped_water += (max_right - height[r])
                else:
                    max_right = height[r]
                r -= 1

        return trapped_water