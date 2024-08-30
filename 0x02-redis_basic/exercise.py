#!/usr/bin/env python3
"""redis"""
import uuid
import redis
from typing import Union, Callable, Optional
import functools


def call_history(method: Callable) -> Callable:
    """getting call history"""
    @functools.wraps(method)
    def wraps(self, *args):
        input_key = '{}:inputs'.format(method.__qualname__)
        output = '{}:outputs'.format(method.__qualname__)
        self._redis.rpush(input_key, str(args))
        get_output = method(self, *args)
        self._redis.rpush(output, str(get_output))
        return get_output
    return wraps


def replay(method: Callable):
    """replay"""
    red_inst = method.__self__._redis
    input_key = '{}:inputs'.format(method.__qualname__)
    output_key = '{}:outputs'.format(method.__qualname__)
    inputs = red_inst.lrange(input_key, 0, -1)
    outputs = red_inst.lrange(output_key, 0, -1)
    print(f'{method.__qualname__} was called {len(inputs)} times')
    for inp, outp in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")  # noqa: E501


def count_calls(method: Callable) -> Callable:
    """wrapper"""
    @functools.wraps(method)
    def wraps(self, *args, **kwargs):
        """wrapper"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wraps


class Cache:
    """cache class"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
