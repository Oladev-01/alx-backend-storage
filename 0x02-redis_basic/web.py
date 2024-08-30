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
    return page.text

if __name__ == "__main__":
    # Test URL with simulated delay
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    print(get_page(url))
    print(f"URL accessed {r.get(f'count:{url}').decode('utf-8')} times")