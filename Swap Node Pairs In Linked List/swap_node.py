class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    save, head.next = head.next, swap_pairs(head.next.next)
    save.next = head
    return save