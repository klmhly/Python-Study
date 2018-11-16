# 难点：倒数k怎么记录
# 解法1，如果知道长度，就可以只走 L-K 步，找到要删除元素的前一个，所以可以先遍历一遍，统计长度。然后第二遍找到插入位置
# 解法2，用两个指针，第一个先走k步。然后两个一起走，这样第一个始终比第二个多走k步，当快指针到末尾了，慢指针就到目标点了
class ListNode():
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 用两个指针，一个先走n步，然后两个一起走，这样两个指针始终相差n，当快的走到末尾时候，慢的就到了目标点
        # 添加一个头节点，这样删除第一个元素就可以和其他的保持一致
        h = ListNode(0)
        h.next = head
        p = h
        q = h
        while n>0:
            p = p.next
            n =n-1
        while p.next is not None:
            p = p.next
            q = q.next
        q.next = q.next.next
        return h.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = l1 = ListNode(2)
    l1.next = l2 = ListNode(3)
    l2.next = l3 = ListNode(4)
    test = Solution()
    res = test.removeNthFromEnd(head,2)
    while res:
        print(res.val)
        res = res.next