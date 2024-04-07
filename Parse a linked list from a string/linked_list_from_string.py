def linked_list_from_string(s):
    for elem in s.split(' -> ')[::-1]:
        if elem!='None':
            next = Node(int(elem), next)
        else:
            next = None
    return next