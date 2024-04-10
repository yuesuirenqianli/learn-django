import hashlib


def get_sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()
