def titleize(phrase):
    lst = phrase.lower().split(' ')
    string = ''
    for el in lst:
        string += el.capitalize()
    return string
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
