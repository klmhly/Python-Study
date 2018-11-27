# 题目：给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
'''
输入: 1->2->3->3->4->4->5
输出: 1->2->5
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 如果是空链表，或者只有1个节点，直接返回
        if head is None or head.next is None:
            return head

        # 本题的关键：新增一个节点，指向head链表，这样方便删除链表头部元素
        s = ListNode(1)
        s.next = head
        flag = 0
        pre = s
        cur = s.next

        # 一个pre指针记录上一个不同的元素，一个cur指针扫描判断
        # 通过flag标志位判断，此时的不等，是前面已经有重复的，还是未有重复的
        while cur.next is not None:
            if cur.val != cur.next.val:
                if flag == 1:
                    pre.next = cur.next
                    cur = cur.next
                    flag = 0
                else:
                    pre = cur;
                    cur = cur.next
            else:
                flag = 1
                cur = cur.next
        if flag == 1:
            pre.next = None
        return s.next

