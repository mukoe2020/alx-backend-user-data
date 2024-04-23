#!/usr/bin/env python3
"""module contains hashing method"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """hash password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """implement auth.register_user
    """
    def __init__(self):
        """constructor"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
