from collections import Counter
from itertools import chain
from re import findall

def analyze(raw_cipher, partial_key={}, top_count=4):
    """Print cipher and top chars, bigrams, and trigrams decrypted via partial
    key. Re-run function, adding keys as they are discovered, until the entire
    cipher returned by the function is decrypted."""

    cipher = raw_cipher.replace(' ', '')
    print partial_decrypt(cipher, partial_key)

    characters = most_frequent_ngrams(cipher, partial_key, top_count)
    print 'Characters: {}'.format(characters)

    all_bigrams = all_ngrams(cipher, 2)
    bigrams = most_frequent_ngrams(all_bigrams, partial_key, top_count)
    print 'Bigrams: {}'.format(bigrams)

    all_trigrams = all_ngrams(cipher, 3)
    trigrams = most_frequent_ngrams(all_trigrams, partial_key, top_count)
    print 'Trigrams: {}'.format(trigrams)

def all_ngrams(cipher, n):
    """Return list of all n-character combinations found in cipher"""

    nested_ngrams = [findall('.'*n, cipher[i:-1]) for i in range(n)]

    return list(chain.from_iterable(nested_ngrams))

def most_frequent_ngrams(cipher, partial_key, top_count):
    """Return list of dicts with top partially decrypted ngrams and count"""

    counter = Counter(cipher)
    freq_list = counter.most_common(top_count)
    most_freq = [{partial_decrypt(freq[0], partial_key): freq[1]} for freq in freq_list]

    return most_freq

def partial_decrypt(cipher, partial_key):
    """Return cipher with any characters in partial key replaced with value"""

    for cipher_char, plain_char in partial_key.items():
        cipher = cipher.replace(cipher_char, plain_char)

    return cipher
