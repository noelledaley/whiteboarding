
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


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
