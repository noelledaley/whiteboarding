
def check_zero_sum(lst):
    """
    Given a list, check if the sum of a list is 0 without using the built-in sum method.

    >>> check_zero_sum([-1, 0, 3, 1, -3])
    True

    >>> check_zero_sum([-1, 0, 3, 3])
    False
    """

    sum = 0

    for num in lst:
        sum += num

    if sum == 0:
        return True

    return False


def check_zero_sum2(lst):
    """Same as above, but try using a second pointer(index) to make more efficient."""


def count_zero_pairs(lst):

    """Count number of zero pairs in a list."""


def count_zero_pairs2(lst):
    """Same as above, but try using a dictionary to make more efficient."""


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
