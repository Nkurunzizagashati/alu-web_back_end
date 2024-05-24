#!/usr/bin/env python3

"""
    a function called filter_datum that returns the log message obfuscated
"""
import re
from typing import List


def filter_datum(fields: List, redaction: string,
                 message: string, separator: string) -> string:
    """
        returns the log message obfuscated

        Args:
        fields (List[str]): A list of strings representing all
        fields to obfuscate.
        redaction (str): A string representing by what the field
        will be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing by which character
        is separating all fields in the log line.
    """
    pattern = '|'.join([f'{field}=[^ {separator}]+' for field in fields])
    return re.sub(pattern, lambda m: f'{m.group().split("=")[0]}={redaction}', message)
