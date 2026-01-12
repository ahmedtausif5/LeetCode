class Solution:
    def maxArea(self, heights: List[int]) -> int:

            area_arr = []

            L, R = 0, len(heights) - 1

            while (L<R):
                length = min(heights[L], heights[R])
                width = R-L
                area = length*width
                area_arr.append(area)

                if heights[L] < heights[R]:
                    L += 1
                else:
                    R -= 1

            return max(area_arr)