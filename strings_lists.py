
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

    # Keep track of all zero pairs in a set. This is more efficient than storing in a list
    # since we can easily check if values are already in the set.
    checked = set()

    for num in lst:
        if num > 0 and -num in lst:
            if (num, -num) not in checked and (-num, num) not in checked:
                checked.add((num, -num))
                count += 1

    return count


def get_smallest(lst):
    """
    Find the smallest integer in a list and return it, without using built-in sort method.

    >>> get_smallest([5, 5, -2, 3])
    -2

    >>> get_smallest([-5, 5, -2, 3])
    -5

    >>> get_smallest([1, 5, 2, 0])
    0

    Runtime: O(n)

    """

    smallest = lst[0]

    for num in lst:
        if num < smallest:
            smallest = num

    return smallest


def get_largest(lst):
    """
    Find the largest integer in a list and return it, without using built-in sort method.

    >>> get_largest([5, 5, -2, 3])
    5

    >>> get_largest([7, -2, 9])
    9

    >>> get_largest([-1, -5, -2, 0])
    0

    Runtime: O(n)

    """

    largest = lst[0]

    for num in lst:
        if num > largest:
            largest = num

    return largest


def is_unique(string):
    """
    Checks that all characters in a string are unique. Returns true/false.

    >>> is_unique('hello')
    False

    >>> is_unique('asdfghjk')
    True

    Runtime: O(n) since we have to convert the string to a set first.
    Checking if the len's are equal is only O(1), though.

    """

    # Converting the string to a set will eliminate any duplicate letters.
    unique_set = set(string)

    # If the length of the original string and the set are equal, we know no duplicates were removed.
    if len(string) == len(unique_set):
        return True

    return False


def urlify(string):
    """
    Replace all the spaces in a string with '%20'.

    >>> urlify('hi i am a string')
    'hi%20i%20am%20a%20string'

    >>> urlify('nope')
    'nope'

    Runtime: O(n) since we have to iterate through all characters.

    """

    new_string = string.split()

    if len(new_string) < 2:
        return string

    new_string = '%20'.join(new_string)

    return new_string


def urlify2(string):
    """
    Replace all the spaces in a string with '%20' without using built-in methods.

    >>> urlify('hi i am a string')
    'hi%20i%20am%20a%20string'

    >>> urlify('nope')
    'nope'

    Runtime: O(n) since we have to iterate through all characters.

    """

    result = ""

    for char in string:
        if char == " ":
            char = '%20'
        result += char

    return result


def is_palindrome(string):
    """
    Checks if a string is a palindrome.

    >>> is_palindrome('banjo')
    False

    >>> is_palindrome('racecar')
    True

    """

    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False

        i += 1
        j -= 1

    return True


def check_permutation(string1, string2):
    """
    Given two strings, check to see if one is a permutation of the other.

    >>> check_permutation('hello', 'loleh')
    True

    >>> check_permutation('this is not', 'a permutation')
    False

    Runtime: O(n) since we're running two loops in succession.

    """

    # Using 2 dictionaries becuase we need to keep track of how many of each letter
    # or space occurs.
    chars = {}
    chars2 = {}

    for char in string1:
        # setdefault will check if a key already exists. If it does, it'll add 1 to that value.
        # if it doesn't, it'll set that value to 0 and add 1.
        chars[char] = chars.setdefault(char, 0) + 1

    for char in string2:
        chars2[char] = chars2.setdefault(char, 0) + 1

    return chars == chars2


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
