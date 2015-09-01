
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

"""
Determine whether or not a linked list has a loop in it.
"""

"""
Given a list, check if the sum of a list is 0 without using the built in sum method.

Try using a second pointer(index) to make more efficient.
"""

"""
Count number of zero pairs in a list.

(Try using a dictionary to make more efficient)
"""
