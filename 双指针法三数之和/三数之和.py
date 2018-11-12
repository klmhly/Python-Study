# 哈希法
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        nums_hash = {}
        result = []
        #  给哈希表赋值{num:次数}
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        # 判断特殊情况
        if (target in nums_hash) :
            if nums_hash[target] >= 3:
                result.append([0, 0, 0])
        # 对数组进行排序
        nums = sorted(list(nums_hash.keys()))
        for i, item in enumerate(nums):
            for j in nums[i + 1:]:
                if item * 2 + j == target and nums_hash[item] >= 2:
                    result.append([item, item, j])
                if item + j * 2 == target and nums_hash[j] >= 2:
                    result.append([item, j, j])
                diff = target - item - j
                if diff in nums_hash and diff > j:
                    result.append([item, j, diff])
        # 对多重列表排序
        result = sorted(result,key=(lambda x:[x[0],x[1]]))
        return result


# 测试
test = Solution()
result = test.threeSum([-1,1,2,-1,-4])
print(result)
