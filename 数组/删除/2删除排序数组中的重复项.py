# 关键排序，所以重复项均在一起
# 双指针-快慢指针
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        length = len(nums)
        # 判断数组长度为0的特殊情况
        if length == 0:
            return 0
        for j in range(1, length):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1
