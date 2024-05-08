# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middle(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head):
            if head is None:
                return head
            prev = None
            curr = head
            nex = curr.next
            while curr:
                curr.next = prev
                prev = curr
                curr = nex
                if nex:
                    nex = nex.next
            return prev

        # Find the middle of the list and reverse the second half
        mid = middle(head)
        secondHalf = reverse(mid)
        
        # Compare the original first half with the reversed second half
        p1 = head
        p2 = secondHalf
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True
