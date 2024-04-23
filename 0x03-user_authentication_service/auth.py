#!/usr/bin/env python3
"""module contains hashing method"""

import bcrypt
import uuid import uuid4
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

    def valid_login(self, email: str, password: str) -> bool:
        """validate login"""
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        except NoResultFound:
            return False
        
    def _generate_uuid() -> str:
    """The function should return a string representation
    of a new UUID. """
    id = str(uuid4())
    return id

    def create_session(self, email: str) -> str:
        """create session"""
        user = self._db.find_user_by(email=email)
        session_id = str(uuid.uuid4())
        self._db.update_user(user.id, session_id=session_id)
        return session_id
