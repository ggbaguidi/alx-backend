#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer
rguments page with default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Simple pagination
        """
        assert (
            isinstance(page, int)
            and isinstance(page_size, int)
            and page > 0
            and page_size > 0
        )
        range_ = index_range(page, page_size)

        if len(self.dataset()) < range_[1]:
            return []
        return self.dataset()[range_[0]:range_[1]]


def index_range(page: int, page_size: int) -> tuple:
    """
    Attributes:
        page(int): the rank of page
        page_size(int): size of each page
    Return:
        (tuple): range of indexes
    """

    return (page_size * (page - 1), page_size * page)
