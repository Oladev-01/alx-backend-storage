#!/usr/bin/env python3
"""redis"""
import uuid
import redis
from typing import Union, Callable, Optional


class Cache:
    """cache class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, int, bytes, float]:
        """get method"""
        value = self._redis.get(key)
        if not value:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """convert key to str"""
        return self._redis.get(key, lambda value: value.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """convert to int"""
        return self._redis.get(key, lambda value: int(value))
