def decode(arr):
    '''
    :param arr: integer representation of encoded password to be decoded
    :return: returns decoded integer
             decoding is the inverse of encoding
    '''

    ENCRYPTION_KEY = 3

    arr_str = ''
    arr_decoded = [(int(elem) - ENCRYPTION_KEY + 10) if (int(elem) < ENCRYPTION_KEY) else (int(elem) - ENCRYPTION_KEY) for elem in str(arr)]
    for i in arr_decoded:
        arr_str += str(i)
    return int(arr_str)
