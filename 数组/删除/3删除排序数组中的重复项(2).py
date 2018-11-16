# 双指针法-快慢指针
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用标志位来记录是不是第二个
        flag = 0
        length = len(nums)
        i = 0
        if length==0:
            return 0
        for j in range(1,length):
            if nums[i]==nums[j] and flag==0:
                i = i+1
                nums[i]=nums[j]
                flag=1
            elif nums[i]!=nums[j]:
                i = i+1
                nums[i]=nums[j]
                flag = 0
        return i+1