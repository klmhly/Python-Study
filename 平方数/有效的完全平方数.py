class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        else:
            low = 1
            high = num
            while low<=high:
                mid = low+ (high-low)//2
                sqrt = num/mid
                if sqrt==mid:
                    return True
                elif mid<sqrt:
                    low = mid+1
                else:
                    high = mid-1
            return False