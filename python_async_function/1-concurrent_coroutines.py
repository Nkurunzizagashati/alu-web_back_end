#!/usr/bin/env python3

"""
    This module contains an async routine called wait_n,
    it takes in 2 int arguments n, and max_delay,
    it will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort() because of concurrency
"""