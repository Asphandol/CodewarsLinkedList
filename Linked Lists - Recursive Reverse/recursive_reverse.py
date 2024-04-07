class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    reversed = None
    while head != None:
        reversed, head.next, head = head, reversed, head.next
    return reversed