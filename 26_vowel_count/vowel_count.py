def vowel_count(phrase):
    new_dict = {}
    vowels = 'aeiou'
    for char in phrase.lower():
        if char in vowels:
            new_dict[char] = new_dict.get(char, 0) + 1
    return new_dict

    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """