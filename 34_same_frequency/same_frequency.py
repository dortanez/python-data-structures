def same_frequency(num1, num2):
    new_lst_1 = list(str(num1))
    new_lst_1.sort()
    new_lst_2 = list(str(num2))
    new_lst_2.sort()
    return new_lst_1 == new_lst_2
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """