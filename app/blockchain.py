hasher = lambda data: data+'*'

class Block:
    def __init__(self, data, hash, lastHash) -> None:
        self.data = data
        self.hash = hash
        self.lastHash = lastHash
    def __repr__(self) -> str:
        return f'[{self.lastHash}] {self.data} ({self.hash})'

class Blockchain:
    def __init__(self) -> None:
        self.chain = [Block('gen-data', 'gen-hash', 'gen-lastHash')]

    def addBlock(self, data):
        self.chain.append(Block(data, hasher(data), self.chain[-1].hash))
    
    def __repr__(self) -> str:
        return '\n'.join([c.__repr__() for c in self.chain])

fooBlockChain = Blockchain()
fooBlockChain.addBlock('one')
fooBlockChain.addBlock('two')
fooBlockChain.addBlock('three')

print(fooBlockChain)