#!/usr/bin/env python3
"""
this is pagination function
"""
from typing import tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index range from a given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return [start, end]