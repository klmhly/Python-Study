'''
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

'''
是在原链表上进行反转，没有开辟新的空间。
每次都先把除掉当前元素的剩下链表存起来，然后把当前元素接到pre的前面。更新pre和p
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        pre = None
        cur = None
        p = head
        while p is not None:
            cur = p.next
            p.next = pre
            pre = p
            p = cur
        return pre
