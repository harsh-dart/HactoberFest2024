class Solution(object):
    def twoSum(self, nums, target):
        valindex={}
        for i,v in enumerate(nums):
            if target-v in valindex:
                return[i,valindex[target-v]]
            valindex[v]=i
        return[-1,-1]
