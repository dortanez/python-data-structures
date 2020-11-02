def flip_case(phrase, to_swap):
    new = ''
    for char in phrase:
        if char == to_swap.upper():
            new += char.lower()
        elif char == to_swap.lower():
            new += to_swap.upper()
        else:
            new += char
    return new

    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
