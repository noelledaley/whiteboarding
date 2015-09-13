
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


def factorial(n):
    """
    Given a number, return its factorial.

    >>> factorial(5)
    120

    >>> factorial(0)
    0
    """

    if n <= 1:
        return n

    return n * factorial(n-1)


def toStr(n, base):
    """
    Given a number and base, return the number in string format.

    >>> toStr(56, 10)
    '56'

    >>> toStr(1453,16)
    '5AD'

    >>> toStr(10, 2)
    '1010'
    """

    conversion = "0123456789ABCDEF"

    # Once n < base, we can look up the corresponding character.
    if n < base:
        return conversion[n]

    return toStr(n/base, base) + conversion[n%base]


def reverse(string):
    """
    Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.

    >>> reverse('hello')
    'olleh'

    >>> reverse('hi there')
    'ereht ih'
    """

    if len(string) == 1:
        return string[0]

    # Important to return the last letter before making the recursive call
    return string[-1] + reverse(string[:-1])


def palindrome(string):
    """
    Using recursion, write a function that takes a string as a parameter and returns True if the string is a palindrome.

    >>> palindrome('kayak')
    True

    >>> palindrome('hello')
    False
    """

    # if len(string) <= 2:
    #     return string[0] == string[-1]

    if not string:
        return True

    return string[0] == string[-1] and palindrome(string[1:-1])


def reverse_list(lst):
    """
    Write a recursive function to reverse a list.

    >>> reverse_list([3, 2, 1])
    [1, 2, 3]

    >>> reverse_list([2, 2, 2, 1])
    [1, 2, 2, 2]
    """

    if len(lst) == 1:
        return lst
    else:
        return [lst[-1]] + reverse_list(lst[:-1])

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
