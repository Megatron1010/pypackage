def sum_array(array):

    '''
    Return sum of all items in array
    Args:
        (array): list or array-like object containing numerical values.


    Returns:
        int: sum of all elements in array.

    Examples:
        >>> sum_array([8, 3, 2, 7, 4])
        24

    '''
    total = 0
    i = 0

    while i < len(array):
        total += array[i]
        i += 1

    return total

#---------------------------------------------------------------------------
def fibonacci(n):


    '''
    Return nth term in fibonacci sequence

Args:
    (n): nth term in fibonacci sequence.


Returns:
    int: nth fibonacci sequence.


    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



#-------------------------------------------------------------------------
def factorial(n):

    '''Return n!'''
    result = 1
    for i in range(1,n+1,1):
        result *= i
    return result


#--------------------------------------------------------------------------
def reverse(word):

    '''Return word in reverse'''
    rev_word =""

    for i in word:
        rev_word = i + rev_word
    return rev_word
