class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
  if source is None: raise ValueError
  return Context(source.next, Node(source.data, dest))