# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head
        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length = length + 1
        k = k % length
        if k==0:
            return head
        tail.next = head
        steps = length - k - 1
        new_tail = head
        for i in range(steps):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
        