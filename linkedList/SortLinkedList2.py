#  https://leetcode.com/problems/reverse-linked-list-ii/submissions/1251709868/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        prev = None 
        current = head
        if current is not None:
            for i in range(left-1):
                prev = current
                current= current.next
        last = prev
        newEnd = current
        nex = current.next
        if current is not None:
            for i in range(right-left+1):
                current.next = prev
                prev = current
                current = nex
                if nex is not None:
                    nex = nex.next
        if last is not None:
            last.next = prev
        else:
            head = prev

        newEnd.next = current 
        return head
         