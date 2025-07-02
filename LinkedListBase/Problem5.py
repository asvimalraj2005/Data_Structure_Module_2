You are given A which is the head of a linked list. Also given is the value B and position C. Complete the function that should insert a new node with the said value at the given position.

Notes:

In case the position is more than length of linked list, simply insert the new node at the tail only.
In case the pos is 0, simply insert the new node at head only.
Follow 0-based indexing for the node numbering.

new_node = ListNode(B)

    if C == 0:
        new_node.next = A
        return new_node

    curr = A
    pos = 0

    while curr is not None and pos < C - 1:
        curr = curr.next
        pos += 1

    if curr is None:
        curr = A
        if curr is None:
            return new_node
        while curr.next:
            curr = curr.next
        curr.next = new_node
    else:
        new_node.next = curr.next
        curr.next = new_node

    return A
