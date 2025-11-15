import asyncio
from functools import wraps
import random

from fastapi import HTTPException

def flaky(odds: float = .5, codes: list = range(500, 509)):
    """
    Makes the endpoint randomly error out, spewing HTTP errors from the `codes` list
    """
    odds = min(odds, 1.0)
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if random.random() <= odds:
                raise HTTPException(random.choice(codes))
            return await func(*args, **kwargs)
        return wrapper
    return decorator

def slow(odds: float = .5, slowness_range: tuple = (.1, 3.0)):
    """
    Makes the endpoint randomly slow
    """
    odds = min(odds, 1.0)
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if random.random() <= odds:
                await asyncio.sleep(random.uniform(*slowness_range))
            return await func(*args, **kwargs)
        return wrapper
    return decorator