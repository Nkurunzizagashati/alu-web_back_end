#!/usr/bin/env python3

"""
    This module contains a function that takes
    a list of sequences and returns a list of tuples,
    where each tuple contains a sequence from
    the input list and its length.
"""

from typing import Iterable
from typing import Sequence
from typing import List
from typing import Tuple
"""
    Imported Iterable, Sequence, List, and Tuple from typing
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list of sequences and returns a list of tuples,
    where each tuple contains a sequence from the input list and its length.
    """

    return [(i, len(i)) for i in lst]
