# 这个题目要求直接在第一个数组上就地修改
# 可以在末尾开辟出需要的空间，每次比较，把大的放在末尾。

class Solution():
    def merge(self,nums1,m,nums2,n):
        # 第一种解法，直接先合并数组然后排序
        # nums1[m:m+n]=nums2[0:]
        # nums1.sort()

        # 第二种解法：在nums1的尾部插入每次的最大值
        i = m-1
        j = n-1
        tail = m+n-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[tail] = nums1[i]
                tail = tail -1
                i = i-1
            else:
                nums1[tail] = nums2[j]
                tail = tail -1
                j = j-1
        if j>=0:
            nums1[0:j+1]=nums2[:j+1]

test = Solution()
# 多出来的几个0是占位
nums1 = [1,4,6,0,0,0,0]
nums2 = [2,4,5,7]
test.merge(nums1,3,nums2,4)
print(nums1)