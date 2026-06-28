class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        su=[]
        a=0
        b=len(nums)
        for i in range (0,b,1):
            a=nums[i]+a
            su.append(a)
        return su