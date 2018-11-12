# 双指针法-首尾指针
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        # 初始化一个很大的差值，在运算过程中更新
        mindiff = 1000
        length = len(nums)
        # 排序
        nums = sorted(nums)
        # 固定一个最小值
        for i, item in enumerate(nums):
            j = i+1
            z = length-1
            # 首尾双指针
            while j<z:
                temp_tag = item + nums[j]+ nums[z]
                diff = abs(target-temp_tag)
                if diff<mindiff:
                    mindiff = diff
                    res = temp_tag
                if temp_tag>target:
                    z = z-1
                elif temp_tag<target:
                    j = j+1
                else:
                    return target
        return res

# 测试
test = Solution()
result = test.threeSumClosest([-1,2,1,-4],1)