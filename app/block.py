from config import GENESIS_DATA


class Block:
    def __init__(self, timestamp, last_hash, hash, data) -> None:
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    @staticmethod
    def genesis():
        return Block(**GENESIS_DATA)
