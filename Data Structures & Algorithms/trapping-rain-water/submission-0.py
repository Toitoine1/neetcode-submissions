class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        vol = 0
        cur_height = min(height[0], height[j])
        while i < j :
            if height[i] < height[j] :
                vol += cur_height - height[i]
                i+=1
                cur_height=min(max(cur_height,height[i]),height[j])
            else :
                vol += cur_height - height[j]
                j+=-1
                cur_height=min(max(cur_height,height[j]),height[i])
            #print(i,j,cur_height,height[i],height[j])
        return vol