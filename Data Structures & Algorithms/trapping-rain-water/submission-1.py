class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_wall = right_wall = water = 0

        while left < right:
            left_height, right_height = height[left], height[right]
            
            if left_height <= right_height:
                if left_wall >= left_height:
                    water += min(left_wall, right_height) - left_height
                else:
                    left_wall = left_height
                left += 1

            elif right_height < left_height:
                if right_wall >= right_height:
                    water += min(right_wall, left_height) - right_height
                else:
                    right_wall = right_height
                right -= 1

        return water
