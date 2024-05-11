#!/usr/bin/env python3

"""
    Augmenting the code with the correct type
    annotation
"""

from typing import Sequence, Any, Union, Optional

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        Augmented this function with the correct type annotation
    """
    if lst:
        return lst[0]
    else:
        return None
