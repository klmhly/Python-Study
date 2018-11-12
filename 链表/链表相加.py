# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = r = ListNode(0)
        carry = 0
        p = l1
        q = l2
        while p or q or carry:
            if p is not None:
                x = p.val
                p = p.next
            else:
                x = 0
            if q is not None:
                y = q.val
                q = q.next
            else:
                y = 0
            s.next = ListNode((x + y + carry) % 10)
            s = s.next
            carry = (x + y + carry) //10
        return r.next

if __name__ =='__main__':
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(3)
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)
    test = Solution()
    res = test.addTwoNumbers(l1,l2)
    while res:
        print(res.val)
        res = res.next