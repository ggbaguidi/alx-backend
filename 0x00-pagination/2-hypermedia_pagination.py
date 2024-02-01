#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Hypermedia pagination
        """

        next_page = None if self.get_page(page, page_size) == [] else page + 1

        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": None if (page - 1) == 0 else page - 1,
            "total_pages": math.ceil(len(self.dataset()) / page_size),
        }


def index_range(page: int, page_size: int) -> tuple:
    """
    Attributes:
        page(int): the rank of page
        page_size(int): size of each page
    Return:
        (tuple): range of indexes
    """

    return (page_size * (page - 1), page_size * page)
