# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 链表非空才操作
        if head is not None:
            # 删除链首特殊情况
            while head.val == val:
                head = head.next
                if head is None:
                    return head
            # 不在链首
            p = head
            n = head.next
            while n:
                if n.val == val:
                    p.next = n.next
                else:
                    p = n
                n = n.next
        return head
# 1->3->2->5
L = ListNode(1)
L.next = L1 = ListNode(3)
L1.next = L2 = ListNode(2)
L2.next = L3 = ListNode(5)

test = Solution()
result = test.removeElements(L,2)
while result:
    print(result.val)
    result = result.next
