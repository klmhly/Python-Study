# 双指针法-首尾指针
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j = j - 1
            else:
                i = i + 1

