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