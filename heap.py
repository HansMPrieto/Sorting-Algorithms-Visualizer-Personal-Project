"""
Heap nodes used for heapsort
"""


def left_child(loc):
    """Gets position of the left child of a node on the heap."""
    left = 2 * loc + 1
    return left


def right_child(loc):
    """Gets position of the right child of a node on the heap."""
    right = 2 * loc + 2
    return right


def parent(loc):
    """Gets position of the parent of a node on the heap."""
    return (loc // 2) - 1

