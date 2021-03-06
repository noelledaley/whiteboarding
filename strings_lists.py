import random


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
    j = len(lst) - 1
    sum = 0

    while i<=j:
        if i == j:
            sum += lst[i]
            i += 1

        sum += lst[i]
        sum += lst[j]
        i += 1
        j -= 1

    if sum == 0:
        return True

    return False


def count_zero_pairs(lst):
    """
    Count number of unique zero pairs in a list.

    >>> count_zero_pairs([1, 0, -1, 2, 2])
    1

    >>> count_zero_pairs([0, -3, 4, -5])
    0

    >>> count_zero_pairs([1, 1, -1, -1, 2, -2, 8, 1])
    2

    Runtime: O(n^2) since we are iterating through lst twice.
    """

    count = 0
    unique_lst = set(lst)

    for num in unique_lst:
        if num > 0 and -num in unique_lst:
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


def check_permutation2(string1, string2):
    """
    Given two strings, check to see if one is a permutation of the other using lists.

    >>> check_permutation('my race car', 'ym ecar rac')
    True

    >>> check_permutation('this is not', 'a permutation')
    False

    Runtime: O(n) since we're running two loops in succession.
    Runtime of sorting lists using built-in method is O(n log(n)).

    """

    lst1 = [char for char in string1]
    lst2 = [char for char in string2]

    return sorted(list1) == sorted(list2)


def get_products(nums):
    """
    Write a function get_products_of_all_ints_except_at_index() that takes an array of integers and returns an array of the products.

    get_products([1, 7, 3, 4])
    [84, 12, 28, 21]

    """

    #TODO


def split(astring, splitter):
    """Split astring by splitter and return list of splits.

    This should work like that built-in Python .split() method [*].
    YOU MAY NOT USE the .split() method in your solution!
    YOU MAY NOT USE regular expressions in your solution!

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

    * Note: the actual Python split method has special behavior
      when it is not passed anything for the splitter -- you do
      not need to implemented that.
    """

    for i in range(len(astring)):
        if astring[i] == splitter:
            word = astring[:i]


def lucky_numbers(n):
    """
    Return n unique random numbers from 1-10 (inclusive).

    Given the numbers 1-10, return n random numbers, making sure to never return the same number twice. You can trust that this function will never be called with n < 0 or n > 10.
    """

    numbers = random.sample(range(1, 11), n)

    return numbers


def merge_sorted_lists(la, lb):
    """
    Given two sorted lists, return a new, fully sorted list.

    merge_sorted_lists([1, 3, 5, 7], [2, 4, 6, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]

    """

    sorted_list = []

    while la and lb:
        if la[0] < lb[0]:
            sorted_list.append(la[0])
            la.pop(0)
        else:
            sorted_list.append(lb[0])
            lb.pop(0)

    return sorted_list


def reverse_list(ls):
    """
    Reverse a list in place.

    >>> reverse_list([1, 2, 3])
    [3, 2, 1]

    >>> reverse_list([-2, -1, 0, 1, 2, 3])
    [3, 2, 1, 0, -1, -2]
    """

    i = 0
    j = len(ls) - 1

    while i < j:
        first = ls[i]
        second = ls[j]
        ls[i] = second
        ls[j] = first
        i += 1
        j -= 1

    return ls

def histogram(string):
    """
    Given a string, return a dictionary where the keys are letters and values are the frequency.
    Do not include spaces.

    >>> sorted(histogram('hackbright academy'))
    ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'k', 'm', 'r', 't', 'y']

    >>> sorted(histogram('banana'))
    ['a', 'b', 'n']
    """

    hist = {}

    for char in string:
        if char == " ":
            continue
        else:
            hist[char] = hist.setdefault(char, 0) + 1

    return hist


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s tests passed!" % result.attempted
    print
