#!/usr/bin/env python3
"""
a function called filter_datum

Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is
"""
import re
from typing import List
from os import environ
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    return re.sub(r'(\b{}\b)'.format('|'.join(fields)), redaction, message)


class RedactingFormatter(logging.Formatter):
    """
      Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.field = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.field, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
