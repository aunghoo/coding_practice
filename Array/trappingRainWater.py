class Solution:
    def trap(self, height: List[int]) -> int:
        # find the highest elevation\
        highest = -1
        highest_i = 0
        for i, h in enumerate(height):
            if h > highest:
                highest = h
                highest_i = i
        # mark the absolute highest elevation on the map
        starting_highest = highest
        starting_highest_i = highest_i

        trapped_water = 0

        # go to the left of the highest elevation and keep getting the trapped waters
        left_highest = 0
        while(left_highest != -1):
            left_highest = -1
            left_highest_i = highest_i
            # search for the highest on the left of current highest elevation
            for l in reversed(range(highest_i)):
                if height[l] > left_highest:
                    left_highest = height[l]
                    left_highest_i = l
            # gather trapped water between the left highest and the highest
            for i in range(left_highest_i+1, highest_i):
                trapped_water += (left_highest - height[i])

            highest_i = left_highest_i
            highest = left_highest


        # gather trapped water on the right side
        highest = starting_highest
        highest_i = starting_highest_i
        right_highest = 0
        while(right_highest != -1):
            right_highest = -1
            right_highest_i = highest_i
            # search for the highest on the right of current highest elevation
            for r in range(highest_i+1, len(height)):
                if height[r] > right_highest:
                    right_highest = height[r]
                    right_highest_i = r
            # gather trapped water between the right highest and the current highest
            for i in range(highest_i+1, right_highest_i):
                trapped_water += (right_highest - height[i])

            highest_i = right_highest_i
            highest = right_highest
            
        return trapped_water