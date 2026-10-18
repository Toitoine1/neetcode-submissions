class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx=0
        i=0
        j=len (heights) -1
        while i != j :
            mx = max(mx, (j-i)*min(heights[j],heights[i]))
            if heights[i]<heights[j]:
                i+=1
            else :
                j+=-1
        return mx
        