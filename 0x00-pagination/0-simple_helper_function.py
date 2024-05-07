#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index corresponding to the range of
    indexes
    Args:
        page (int): current page
        page_size (int): size of items in a page
    Returns:
        (tuple): return a tuple of size two containing a start index
        and an end index for the given page
    """
    nextPageStart = page * page_size
    return nextPageStart - page_size, nextPageStart
