#!/usr/bin/env python3
"""module contains hashing method"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

def _hash_password(password: str) -> bytes:
    """hash password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())