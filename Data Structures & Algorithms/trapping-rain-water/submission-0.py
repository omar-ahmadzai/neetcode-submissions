class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_wall = 0
        right_wall = 0

        water = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]

            if left_height <= right_height:
                if left_wall >= left_height:
                    water += right_height - left_height if right_height <= left_wall else left_wall - left_height
                else:
                    left_wall = left_height
                left += 1

            elif right_height < left_height:
                if right_wall >= right_height:
                    water += left_height - right_height if left_height <= right_wall else right_wall - right_height
                else:
                    right_wall = right_height
                right -= 1

        return water
