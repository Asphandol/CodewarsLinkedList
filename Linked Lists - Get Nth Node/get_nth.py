from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node == None:
        raise Exception
    i = 0
    current = node
    while i != index:
        current = current.next
        i+=1
        if current.data == None:
            raise Exception
    return current