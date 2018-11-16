# 双指针法-快慢指针
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i= 0
        length = len(nums)
        if length == 0:
            return 0
        for j in range(length):
            if nums[j]!=val:
                nums[i]=nums[j]
                i=i+1
        return i