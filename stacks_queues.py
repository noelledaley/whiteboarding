
def reverse_stack(string):
    """Use a stack to reverse a string.

    >>> reverse_stack('hello')
    'olleh'

    >>> reverse_stack('one more time')
    'emit erom eno'
    """

    old_string = list(string)

    new_string = []

    while old_string:
        char = old_string.pop()
        new_string.append(char)

    new_string = "".join(new_string)

    return new_string


def hot_potato(namelist, num):
    """
    Using a queue, return the name of the last person remaining after repetitive counting by num.

    >>> hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7)
    'Susan'
    """

    # As long as there is at least one player left
    while len(namelist) > 1:

        for i in range(num):
            # The person at the front passes the potato and moves to the back of the queue
            front = namelist.pop(0)
            namelist.append(front)
        # After num number of passes, remove the person at the front of the queue,
        # since they have the potatoe
        namelist.pop(0)

    return namelist[0]


def palindrome_deque(string):
    """
    Using a deque, check if a string is a palindrome.

    >>> palindrome_deque('radar')
    True

    >>> palindrome_deque('dfsdf')
    False
    """

    chars = list(string)

    while len(chars) > 1:
        first = chars.pop(0)
        last = chars.pop()
        if first != last:
            return False

    return True

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
