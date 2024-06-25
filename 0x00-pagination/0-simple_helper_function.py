#!/usr/bin/env python3
"""
this is pagination function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index range from a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)