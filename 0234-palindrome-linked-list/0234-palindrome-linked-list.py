# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        curr = head
        s = []
        while curr is not None:
            s.append(curr.val)
            curr = curr.next
        while head is not None:
            c = s.pop()
            if head.val != c:
                return False
            head = head.next
        return True
        