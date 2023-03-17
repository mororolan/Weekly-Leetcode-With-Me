# -*- coding: utf-8 -*-
# @File    : 02_List_add_two_numbers.py
# @Author  : Robin Lan
# @Time    : 17/3/23 23:03
# @Software: PyCharm
# @Description: Add Two Numbers

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        pointer = res
        carry = 0
        tmp = 0
        while l1 or l2 or carry:
            # if l1 and l2:
            #     tmp = l1.val + l2.val + carry
            # elif l1:
            #     tmp = l1.val + carry
            # elif l2:
            #     tmp = l2.val + carry
            # else:
            #     tmp = carry
            sum_a = l1.val if l1 else 0
            sum_b = l2.val if l2 else 0
            tmp = sum_a + sum_b + carry

            carry = tmp // 10
            tmp = tmp % 10

            # carry  = 0
            # if tmp > 9:
            #     carry = 1
            #     tmp = tmp - 10

            pointer.next = ListNode(tmp)
            pointer = pointer.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next




