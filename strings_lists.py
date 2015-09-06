
def check_zero_sum(lst):
    """
    Given a list, check if the sum of a list is 0 without using the built-in sum method.

    >>> check_zero_sum([-1, 0, 3, 1, -3])
    True

    >>> check_zero_sum([-1, 0, 3, 3])
    False

    Runtime: O(n) since we're iterating through each item in list.
    """

    sum = 0

    for num in lst:
        sum += num

    if sum == 0:
        return True

    return False


def check_zero_sum2(lst):
    """
    Same as above, but try using a second pointer(index) to make more efficient.

    >>> check_zero_sum([-1, 0, 3, 1, -3])
    True

    >>> check_zero_sum([-1, 0, 3, 3])
    False

    Runtime: O(log n)? since we're iterating through 1/2 of the list.

    """

    i = 0
    j = 0
    sum = 0

    while i<j:
        sum += lst[i]
        sum += lst[j]
        i += 1
        j -= 1

    if sum == 0:
        return True

    return False


def count_zero_pairs(lst):
    """
    Count number of zero pairs in a list.

    >>> count_zero_pairs([1, 0, -1, 2, 2])
    1

    >>> count_zero_pairs([0, -3, 4, -5])
    0

    >> count_zero_pairs([1, 1, -1, -1, 2, -2])
    3

    Runtime: O(n^2) since we are iterating through lst twice.
    """

    count = 0

    checked = set()

    for num in lst:
        if num > 0 and -num in lst:
            if (num, -num) not in checked and (-num, num) not in checked:
                checked.add((num, -num))
                count += 1

    return count


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
