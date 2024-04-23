#!/usr/bin/env python3
"""
In this task you will define a _hash_password method that takes
in a password string arguments and returns bytes
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def hash_password(password: str) -> bytes:
    """
    Hashes a password with bcrypt
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
