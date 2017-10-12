import unittest
import bcrypt
from src.login import UserManager

def test_add_user():
    um = UserManager()
    name = um.add_user("test", "test", "test", "test")
    assert name == ("test", "test", "test", "test")

def test_validate_credentials():
    vc = UserManager()
    vcred = vc.validate_credentials("test", "test")
    assert vcred == ("test", "test")

def test_hash_password():
    pw = UserManager()
    hash = pw._hash_password(bcrypt.gensalt())
    assert hash == (bcrypt.gensalt())