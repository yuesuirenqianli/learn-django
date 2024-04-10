import hashlib
import random

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


def gen_random_code(length=4):
    return ''.join(random.choices(ALL_CHARS, k=length))
