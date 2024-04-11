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
import mysql.connector

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


def get_logger() -> logging.Logger:
    """
      Function that creates a custom logger, and
      sets it format, level and gives it handler.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.propagate = False
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
      A function that uses mysql connector driver,
      to connect to a database
    """
    usrname = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    passwrd = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    hostname = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")

    con = mysql.connector.connection.MySQLConnection(user=usrname,
                                                     password=passwrd,
                                                     host=hostname,
                                                     database=db_name)
    return con


