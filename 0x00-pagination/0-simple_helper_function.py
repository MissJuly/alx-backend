#!/usr/bin/env python3
"""API Design: Pagination module"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Helper function that return a tuple of page and
    page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
