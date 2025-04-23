import hashlib
from Variables import hash_count


def hash_data(data):
    hashed_data = data
    for x in range(hash_count):
        hashed_data = hashlib.sha3_256(hashed_data.encode('ascii')).hexdigest()
    return hashed_data
