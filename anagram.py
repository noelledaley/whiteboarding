"""Given a word list, find the word with the most anagrams in the list."""

def find_most_anagrams_from_wordlist(wordlist):
    """Given a list of words, return the word with the most anagrams.

    For a list of ['act', 'cat', 'bill']:
    - 'act' and 'cat' are anagrams, so they both have 2 matching words.
    - 'bill' has no anagrams, os it has one matching word (itself).

    Given that 'act' is the first instance of the most-anagrammed word,
    we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

    Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'
    """

    anagrams = {}

    for word in wordlist:
        anagrams[tuple(sorted(word))] = anagrams.setdefault(tuple(sorted(word)), 0) + 1

    most_frequent = max(anagrams.vals())

    for word in wordlist:
        if anagrams[word] == most_frequent:
            return word


def find_most_anagrams_from_wordlist(wordlist):
    """Given a list of words, return the word with the most anagrams according to words.txt.

    For a list of ['act', 'cat', 'bill']:
    - 'act' and 'cat' are anagrams, so they both have 2 matching words.
    - 'bill' has no anagrams, os it has one matching word (itself).

    Given that 'act' is the first instance of the most-anagrammed word,
    we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

    Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'
    """

    all_words = [w.strip() for w in open('words.txt')]

    # Anagrams are two words that contain all the same letters.
    # This means that if you sort two anagram words, they should contain the same letters in the same order.

    # Create dictionary where keys are tuple of chars and values are number anagrams
    # eg. ('g', 'h', 'h', 'i', 't'): 2
    anagrams_count = {}

    for word in all_words:
        anagrams_count[tuple(sorted(word))] = anagrams_count.setdefault(tuple(sorted(word)), 0) + 1


    # Now that we have our dict, we can look up each input word
    # and see how many possible anagrams there are.
    anagram_word = wordlist[0]
    most_anagrams = anagrams_count.get(tuple(sorted(anagram_word))) or 0

    for word in wordlist:

        num_anagrams = anagrams_count.get(tuple(sorted(word)))
        if num_anagrams > most_anagrams:
            most_anagrams = num_anagrams
            anagram_word = word

    return anagram_word


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
