# 双指针法-首尾指针
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # (差值，索引)  ，代表这个索引的属，需要配对的差值，
        # 遍历到一个数字时，先判断差值在不在哈希表，在则找到了；
        # 没在，则继续遍历下一个数
        diff_hash = {}
        for i ,item in enumerate(nums):
            diff = target - item
            if item in diff_hash:
                return [diff_hash[item],i]
            else:
                diff_hash[diff] = i