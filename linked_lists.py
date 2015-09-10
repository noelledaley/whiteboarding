from data_structures import LinkedList, Node, animals, cities, numbers, dog

def print_all(ll):
    """Print all nodes in a LinkedList.

    >>> print_all(animals)
    dog
    cat
    bird
    cow
    zebra
    >>>

    Runtime: O(n)

    """

    current = ll.head
    while current:
        print current.data
        current = current.next


def add_node(ll, data):
    """
    Add node to LinkedList with no tail.

    >>> add_node(animals, 'zebra')
    dog
    cat
    bird
    cow
    zebra

    Runtime: O(n)
    """

    current = ll.head

    while current.next:
        current = current.next

    current.next = Node(data)

    print_all(ll)


def remove_node(ll, data):
    """Remove node from LinkedList with given data.

    >>> remove_node(animals, 'zebra')
    dog
    cat
    bird
    cow

    Runtime: O(n)
    """

    current = ll.head

    # If the head contains the data we're looking for, replace head with next Node.
    if current.data == data:
        current = current.next
        return

    while current.next:

        if current.next.data == data:
            current.next = current.next.next
        else:
            current = current.next

    print_all(ll)


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


def reverse(head):
    """
    Write a function that takes the head node of a linked list and returns the head of a new, reversed linked list.

    >>> reverse(dog)
    'cow'
    """

    # Create new LinkedList, add current head but set next as None (since this will be new tail)
    reversed_ll = LinkedList()
    new_tail = head
    new_tail.next = None
    add(revsersed_ll, new_tail)

    current = head

    while current.next:
        new_node = Node(current.next)
        new_node.next = current


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
