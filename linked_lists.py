from data_structures import LinkedList, Node, animals, cities

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

    """

    current = ll.head
    checked = set()
    checked.add(current)

    while current.next:
        if current.next not in checked:
            checked.add(current.next)
        else:
            return True

    return False


def remove_duplicates(ll):
    """Given a linked list, remove duplicates."""

    current = ll.head
    print 'starting with:', current

    # Use a set to check if we've already checked a node.
    checked = set()
    checked.add(current)

    while current.next:
        print 'looking at: ', current
        print 'current.next is: ', current.next
        print current.next, 'not in checked?', current.next not in checked

        if current.next not in checked:
            checked.add(current.next)
            print 'added'

        # FIXME!
        else:
            print 'duplicate!'
            print 'current.next was', current.next
            current.next = current.next.next
            print 'but current.next is now', current.next
            break

        current = current.next


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
