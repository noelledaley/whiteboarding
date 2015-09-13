def find_sum(lst):
    """Given a list of integers, return the sum of the list using recursion.

    >>> find_sum([0, 1, 2])
    3

    >> find_sum([-2, -3, -1])
    -6
    """

    if len(lst) == 1:
        return lst[0]

    return lst[0] + find_sum(lst[1:])


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
