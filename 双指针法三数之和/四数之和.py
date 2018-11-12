# 双指针法-首尾指针
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        res_set = []
        length = len(nums)
        # 对数组排序
        nums = sorted(nums)
        # 固定前两个最小数
        for i, item1 in enumerate(nums):
            for j in range(i+1,length):
                a = j+1
                z = length-1
                # 首尾双指针
                while a<z:
                    tag = item1+nums[j]+nums[a]+nums[z]
                    if tag == target:
                        result.append([nums[i],nums[j],nums[a],nums[z]])
                        a = a+1
                        z = z-1
                    elif tag < target:
                        a = a+1
                    else:
                        z = z-1
        # 对二维列表去重
        for item in result:
            if item not in res_set:
                res_set.append(item)
        return res_set

# 测试
test = Solution()
result = test.fourSum([-1,-1,2,0,3,-1],0)
print(result)