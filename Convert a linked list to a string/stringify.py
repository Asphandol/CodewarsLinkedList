def stringify(node):
    if node == None:
        return 'None'
    string = str(node.data)
    node = node.next
    try:
        while 1:
            string += ' -> ' + str(node.data)
        node = node.next
    except:
        return string + ' -> None'