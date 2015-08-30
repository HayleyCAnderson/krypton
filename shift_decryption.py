def blunt_force_shift(cipher):
    """Print all possible shift decryptions of cipher."""

    for n in range(0, 26):
        shift(cipher, n)

def shift(cipher, n):
    """Print n-character shift of cipher."""

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    rotated_string = ''

    for char in cipher:
        try:
            shifted_index = alphabet.index(char) + n
            if shifted_index > 26 - 1:
                shifted_index -= 26

            rotated_string += alphabet[shifted_index]
        except ValueError:
            rotated_string += char

    print '{}-char shift: {}'.format(n, rotated_string)
