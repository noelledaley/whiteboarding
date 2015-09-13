
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

    

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
