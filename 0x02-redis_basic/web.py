#!/usr/bin/env python3
"""getting from a page"""

import requests
import redis
from typing import Callable
import functools

r = redis.Redis()


def count_cache(method: Callable) -> Callable:
    """getting count"""
    @functools.wraps(method)
    def wraps(url: str) -> str:
        """wrapper"""
        r.incr(f"count:{url}")
        page = r.get(url)
        if page:
            return page.decode('utf-8')
        else:
            page = method(url)
            r.setex(url, 10, page)
            return page
    return wraps


@count_cache
def get_page(url: str) -> str:
    """function to get page"""
    page = requests.get(url, timeout=10)
    return str(page)
