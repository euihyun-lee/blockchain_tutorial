import hashlib, struct
from datetime import datetime
# import Meta
import json

class Block():
    def __init__(self, block_hash, header):
        self.block_hash = block_hash    # str, hash of this block
        self.header = header    # class Header

    def __str__(self):
        return "<Block with hash value %s>" % (self.block_hash)

class Header():
    def __init__(self, index, timestamp, prev_block, nonce, mrkl_root):
        self.index = index  # int
        self.timestamp = timestamp  # str(datetime.datetime.now())
        self.prev_block = prev_block    # str, hash of previous block
        self.nonce = nonce  # int
        self.mrkl_root = mrkl_root  # = data, for later work
        self.data = mrkl_root   # list of dictionary (or json style string)

def calcHash(header):
    header_pack = "%d%s%s%d%s" % (header.index, header.timestamp, header.prev_block, header.nonce, header.mrkl_root)
    sha = hashlib.sha256()
    sha.update(header_pack.encode('utf-8'))
    
    return sha.hexdigest()

def genesisBlock():
    header = Header(0, str(datetime.now()), "0", 9, None)
    return Block(calcHash(header), header)

def blockToJSON(block):
    return json.dumps({"block_hash": block.block_hash ,"header": {"index": str(block.header.index), "timestamp": block.header.timestamp, "prev_block": block.header.prev_block, "nonce": block.header.nonce, "data": block.header.data}}, indent=4)

def JSONToBlock(block_json):
    block_json = json.loads(block_json)
    header_json = block_json["header"]
        
    header = Header(int(header_json["index"]), header_json["timestamp"], header_json["prev_block"], int(header_json["nonce"]), header_json["data"])
    return Block(block_json["block_hash"], header)

def clarifyChain(chain):
    new_chain = []
    for block in chain:
        block = JSONToBlock(block)

        print(block)
        new_chain.append(block)

    return new_chain
