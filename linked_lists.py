
def remove_duplicates(ll):
    """Given a linked list, remove duplicates."""

    current = ll.head

    # Use a set to check if we've already checked a node.
    checked = set()
    checked.add(current)

    while current.next:

        if current.next not in checked:
            checked.add(current.next)

        elif:
            current.next = current.next.next

        current = current.next
