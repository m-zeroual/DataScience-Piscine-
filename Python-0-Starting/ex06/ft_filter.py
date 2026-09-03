def ft_filter(function, iterable):
    """Return an iterator that filters elements using a function."""
    if function is None:
        return iter([item for item in iterable if item])

    return iter([item for item in iterable if function(item)])
