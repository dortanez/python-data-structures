def repeat(phrase, num):
    if type(num) is not int or num < 0:
        return None
    string = ''
    for n in range(0,num):
        string += phrase
    return string
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
