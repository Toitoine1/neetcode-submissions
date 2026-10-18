class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        workingvalues = []
    
        nums.sort()
        n = len(nums)
        for k in range(n-2):
            i = k+1
            j = n-1
            while i < j :
                if (nums[i]+nums[j]) == -nums[k] :
                    workingvalues.append((nums[k],nums[i],nums[j]))
                    i+=1
                    j+=-1
                elif (nums[i]+nums[j]) < -nums[k] :
                    i+=1
                else :
                    j += -1

        return(list(set(workingvalues)))
