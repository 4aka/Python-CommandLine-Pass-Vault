import hashlib


def hash_data(data):
    hashed_data = data
    for x in range(50):
        hashed_data = hashlib.sha3_256(hashed_data.encode('ascii')).hexdigest()
    return hashed_data
