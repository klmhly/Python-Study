# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 如果存在空链表，则简单的返回
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return
        # 一个头节点，一个活动指针
        head = l3 = ListNode(0)
        # 同时遍历两个链表进行比较
        while l1 and l2:
            if l1.val<=l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1 is not None:
            l3.next = l1
        else:
            l3.next = l2
        return head.next


L1 = ListNode(1)
L1.next = L11 = ListNode(2)
L11.next = L12 = ListNode(4)
L2 = ListNode(1)
L2.next = L21 = ListNode(3)
L21.next = L22 = ListNode(5)
test = Solution()
l3 = test.mergeTwoLists(L1,L2)
while l3:
    print(l3.val)
    l3 = l3.next