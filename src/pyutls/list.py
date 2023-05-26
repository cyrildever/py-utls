def chunk(items, size):
    """Split a list into chunks of a maximum size"""
    return [items[i: i + size] for i in range(0, len(items), size)]


def flatten(t):
    """Flatten a list of list"""
    return [item for sublist in t for item in sublist]
