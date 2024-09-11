from app.block import Block
from config import GENESIS_DATA


class TestBlock:
    timestamp = "a-date"
    last_hash = "foo-hash"
    hash = "bar-hash"
    data = ["blockchain", "data"]
    block = Block(timestamp, last_hash, hash, data)

    def test_has_timestamp_lasthash_data_block(self):
        assert self.block.timestamp == self.timestamp
        assert self.block.last_hash == self.last_hash
        assert self.block.hash == self.hash
        assert self.block.data == self.data

    class TestGenesis:
        genesis = Block.genesis()

        def test_returns_block_instance(self):
            assert isinstance(self.genesis, Block)

        def test_returns_genesis_data(self):
            assert self.genesis == Block(**GENESIS_DATA)
