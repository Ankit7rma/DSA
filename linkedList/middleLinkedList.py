def middle(head):
    f = head
    s = head
    while s and s.next:
        f = f.next
        s = s.next.next
    return f