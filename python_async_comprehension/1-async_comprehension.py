#!/usr/bin/env python3

"""
    This module contains a coroutine that takes no
    argument. The coroutine will collect 10 random
    numbers using an async comprehensing over, then
    return the 10 random numbers

    I am also importing async_generator from
    0-async_generator.py
"""

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


def async_comprehension() -> List:
    """
        This coroutine coroutine will collect 10 random numbers
        using an async comprehensing over async_generator,
        then return the 10 random numbers
    """

    return [i async for i in async_generator()]
