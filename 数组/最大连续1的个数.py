class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = count + 1
            else:
                max_count = max(max_count, count)
                count = 0
        # 不要忘记，最后一次更新的count也需要进行一次比较
        max_count = max(max_count,count)
        return max_count

nums = [1]
test = Solution()
rel = test.findMaxConsecutiveOnes(nums)
print(rel)