def list_check(lst):
   return [item for item in lst if type(item) is list] == lst
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
