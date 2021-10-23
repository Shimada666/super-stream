from typing import TypeVar

T = TypeVar('T')


def identity(x: T) -> T:
    """
    :param x:
    :return: itself, is equivalent to lambda x: x
    """
    return x
