#!/usr/bin/env python3

"""Module for implementing an expiring web cache and tracker"""

import requests
import redis
from functools import wraps
from typing import Callable

# Initialize Redis client
redis_client = redis.Redis()

def cache_page(expiration: int = 10):
    """
    Decorator to cache the result of a function for a specified expiration time.

    Args:
        expiration (int): Time in seconds for the cache to expire.
    """
    def decorator(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(url: str, *args, **kwargs) -> str:
            """
            Wrapper function to handle caching of the page content.

            Args:
                url (str): The URL to get the page content from.

            Returns:
                str: The HTML content of the page.
            """
            cache_key = f"cache:{url}"
            cached_page = redis_client.get(cache_key)
            if cached_page:
                return cached_page.decode('utf-8')

            # Call the original method to get the page content
            page_content = method(url, *args, **kwargs)
            redis_client.setex(cache_key, expiration, page_content)
            return page_content
        return wrapper
    return decorator

def count_access(method: Callable) -> Callable:
    """
    Decorator to count the number of times a URL is accessed.

    Args:
        method (Callable): The function to wrap.
    """
    @wraps(method)
    def wrapper(url: str, *args, **kwargs) -> str:
        """
        Wrapper function to count accesses to the URL.

        Args:
            url (str): The URL to count accesses for.

        Returns:
            str: The HTML content of the page.
        """
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return method(url, *args, **kwargs)
    return wrapper

@cache_page(expiration=10)
@count_access
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a given URL.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.text
