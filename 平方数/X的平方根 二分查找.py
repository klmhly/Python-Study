class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:
            return x
        low = 1
        high = x
        while low<=high:
            mid = low + (high-low)//2
            sqrt = x//mid
            if sqrt==mid:
                return sqrt
            elif mid<sqrt:
                low = mid +1
            else:
                high = mid-1
        return high