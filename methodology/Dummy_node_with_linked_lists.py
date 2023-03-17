# -*- coding: utf-8 -*-
# @File    : Dummy_node_with_linked_lists.py
# @Author  : Robin Lan
# @Time    : 17/3/23 22:46
# @Software: PyCharm
# @Aim: simplify the edge cases when dealing with the head node.

# Since the head node does not have a previous node,
# it requires special handling in certain situations like insertion and deletion.

'''
 when inserting a new node at the beginning of the linked list,
 Before: we need to check if the head node exists and handle it separately.
 After:  with a dummy node, we can simply insert the new node after the dummy node,
         and the dummy node will always be there to act as the new head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_node_at_head(head, val):
    new_node = ListNode(val)
    if not head:
        head = new_node
    else:
        new_node.next = head
        head = new_node
    return head

def insert_node_at_tail(head, val):
    new_node = ListNode(val)
    if not head:
        head = new_node
    else:
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    return head

'''Scope: remove the first node with the given value
   Input: head = [1,2,3,4,5], val = 3
   Output: [1,2,4,5]'''

class Solution:
    def removeNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                break
            cur = cur.next
        return dummy.next

    def removeNode_without_dummy(self, head: ListNode, val: int) -> ListNode:
        if head and head.val == val:
            return head.next
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head