#!/usr/bin/env python3

"""Module for Redis storage"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """
        Initialize the Cache class.

        Creates an instance of the Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key and optionally apply a conversion function.

        Args:
            key (str): The key to look up in Redis.
            fn (Optional[Callable]): The function to apply to the retrieved data.

        Returns:
            Union[str, bytes, int, float, None]: The data stored in Redis, potentially converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis by key.

        Args:
            key (str): The key to look up in Redis.

        Returns:
            Optional[str]: The string data stored in Redis or None if key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis by key.

        Args:
            key (str): The key to look up in Redis.

        Returns:
            Optional[int]: The integer data stored in Redis or None if key does not exist.
        """
        return self.get(key, fn=int)
