def ft_filter(function, iterable):
    """Return an iterator that filters elements using a function."""
    if function is None:
        return iter([item for item in iterable if item])

    return iter([item for item in iterable if function(item)])




def is_even(number):
    if number is int:
        return number % 2 == 0
    return False


numbers = [1, 2, None, " ", 4, 5, 6]

result = filter(is_even, numbers)

for item in result:
    print(item, end='\n')
