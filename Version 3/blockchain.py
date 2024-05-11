# -*- coding: utf-8 -*-

import pickle
from hashlib import sha256

def createhash(*args):
    '''
    Creates a SHA256 hash of all the arguments.
    '''
    hashing_text = "-".join([str(x) for x in args])
    h = sha256()
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

class EdBlock():
    data = None 
    hash = None 
    nonce = 0
    previous_hash = "0" * 64 # Initial Hash

    def __init__(self, data, block_num=0):
        self.data = data
        self.block_num = block_num

    def hash(self):
        return createhash(
            self.previous_hash, 
            self.block_num, 
            self.data, 
            self.nonce
        )
    
    # String function to print the contents of the block, instead of printing an object
    def __str__(self):
        return str("Block#: %s\nHash: %s\nPrevious Hash: %s\nData: %s\nNonce: %s\n" % (
            self.block_num, 
            self.hash(), 
            self.previous_hash, 
            self.data, 
            self.nonce
            )
        )

class EdBlockChain():
    difficulty = 5 # Number of zeros at the start of the hash value

    def __init__(self, chain=[]):
        self.chain = chain 

    def add(self, block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass # 'chain' is empty

        # Loop infinitely until Nonce produces desired hash
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break 
            else:
                block.nonce += 1

    def isValid(self):
        for i in range(1, len(self.chain)):
            _previous = self.chain[i].previous_hash # Protected variable
            _current = self.chain[i-1].hash()

            if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
                return False
            
        return True

def save_blockchain(blockchain):
    with open('BlockchainData/blockchain.pkl', 'wb') as file:
        pickle.dump(blockchain, file)

def load_blockchain():
    with open('BlockchainData/blockchain.pkl', 'rb') as file:
        blockchain = pickle.load(file)
    return blockchain

def main():
    # Transactions
    blockchain = EdBlockChain()
    database = []

    for i, data in enumerate(database):
        blockchain.mine(EdBlock(data, i))

    for block in blockchain.chain:
        print(block)

    save_blockchain(blockchain)

    # Corrupting the block
    # blockchain.chain[2].data = "NEW DATA"
    # blockchain.mine(blockchain.chain[2])
    # print(blockchain.isValid())

if __name__ == '__main__':
    main()