from data_structures import LinkedList, Node, animals, cities, numbers

def print_all(ll):
    """Print all nodes in a LinkedList.

    >>> print_all(animals)
    dog
    cat
    bird
    cow
    >>>

    """

    current = ll.head
    while current:
        print current.data
        current = current.next


def has_loop(ll):
    """
    Determine whether or not a linked list has a loop in it.

    >>> has_loop(cities)
    True

    >>> has_loop(animals)
    False

    """

    current = ll.head
    checked = set()
    checked.add(current)

    while current.next:

        if current.next not in checked:
            checked.add(current.next)
            current = current.next
        else:
            return True

    return False


def remove_duplicates(ll):
    """Given a linked list, remove duplicate values.

    >>> remove_duplicates(numbers)
    set([1, 2, 3, 4])

    """

    current = ll.head

    # Use a set to check if we've already checked a node.
    checked = set()
    checked.add(current.data)

    while current.next:

        if current.next.data not in checked:
            checked.add(current.next.data)
            current = current.next

        else:
            current.next = current.next.next

    return checked


"""
Given a list, check if the sum of a list is 0 without using the built in sum method.

Try using a second pointer(index) to make more efficient.
"""

"""
Count number of zero pairs in a list.

(Try using a dictionary to make more efficient)
"""

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
