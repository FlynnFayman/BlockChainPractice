import datetime as d
import hashlib as h 

#The idea came from source: medium.datadriveninvestor.com/is-it-hard-to-build-a-blockchain-from-scratch-23bac74e4f

class Block:
    def __init__(self,index,timestamp,data,prevhash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash
        self.hash = self.hashblock()
    def hashblock(self):
        block_encryption = h.sha256()
        block_encryption.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.prevhash).encode('utf-8'))
        return block_encryption.hexdigest()
    @staticmethod 
    # The static methode below will genrate a genesis block
    def genesisblock():
        return Block(0,d.datetime.now(),"genesis block transaction"," ")
    @staticmethod
    def newblock(lastblock): #get the next block that comes after
        index = lastblock.index + 1
        timestamp = d.datetime.now()
        hashblock = lastblock.hash 
        data = "Transaction " + str(index)
        return Block(index,timestamp,data,hashblock)
    
blockchain = [Block.genesisblock()]
prevblock = blockchain[0]


#Creating a Block Chain

for i in range (0,6):
    addblock = Block.newblock(prevblock)
    blockchain.append(addblock)
    prevblock = addblock

    print("Block ID #{} ".format(addblock.index)) # show the block id
    print("Timestamp:{}".format(addblock.timestamp))# show the block timestamp
    print("Hash of the block:{}".format(addblock.hash))# show the hash of the added block
    print("Previous Block Hash:{}".format(addblock.prevhash))# show the previous block hash
    print("data:{}\n".format(addblock.data))#