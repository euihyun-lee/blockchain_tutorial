from blockchain import Block, Header, calcHash, genesisBlock, blockToJSON, clarifyChain

import json, requests
from datetime import datetime
from flask import Flask
from flask import request
node = Flask(__name__)

miner_address = "something-like-hash-address"
node_chain = [genesisBlock()]
node_transactions = []
peer_nodes = []
peer_servers = ['localhost:8080']

# TODO: modify PoW - currently very simple work
def PoW(last_proof):
    inc = last_proof + 1
    while not (inc % 9 == 0 and inc % last_proof == 0):
        inc += 1
    
    return inc

# TODO: Validation process
def validate():
    pass

# Peer node search process
@node.route('/find_peers', methods = ['GET'])
def findPeers():
    # get peer from on-line server and get peer from existing peers
    host = request.host
    print(host)
    headers = {'Content-Type': 'application/json'}
    data = {'miner': True, 'url': host}
    for server in peer_servers:
        response = requests.post("http://" + server + '/get_peers', data=json.dumps(data), headers=headers)
        peers = json.loads(response.content)
        for peer in peers:
            if peer == host:
                continue
            if not peer in peer_nodes:
                peer_nodes.append(peer)

    return json.dumps(peer_nodes, indent=4)

@node.route('/mine', methods = ['GET'])
def mine():
    consensus()

    last_block = node_chain[-1]
    last_proof = last_block.header.nonce
    proof = PoW(last_proof)
    node_transactions.append({"from": "network", "to": miner_address, "amount": 1})

    new_block_nonce = proof
    new_block_data = list(node_transactions)
    new_block_index = last_block.header.index + 1
    new_block_timestamp = str(datetime.now())
    last_block_hash = last_block.block_hash

    node_transactions[:] = []

    new_block_header = Header(new_block_index, new_block_timestamp, last_block_hash, new_block_nonce, new_block_data)
    mined_block = Block(calcHash(new_block_header), new_block_header)

    node_chain.append(mined_block)

    return blockToJSON(mined_block)

@node.route('/tx', methods=['POST'])
def transaction():
    new_tx = request.get_json()
    node_transactions.append(new_tx)

    print("New transaction")
    print("FROM: {}".format(new_tx['from'].encode('ascii','replace')))
    print("TO: {}".format(new_tx['to'].encode('ascii','replace')))
    print("AMOUNT: {}\n".format(new_tx['amount']))

    return "Transaction submission successful\n"

@node.route('/get_chain', methods=['GET'])
def getChain():
    sending_chain = []
    for block in node_chain:
        sending_chain.append(blockToJSON(block))

    return json.dumps(sending_chain, indent=4)
        
def findChains():
    other_chains = []
    for node in peer_nodes:
        chain = json.loads(requests.get("http://" + node + "/get_chain").content)
        chain = clarifyChain(chain)
        other_chains.append(chain)
    return other_chains

def consensus():
    global node_chain

    findPeers()
    other_chains = findChains()
    
    longest = node_chain
    for chain in other_chains:
        if len(longest) < len(chain):
            longest = chain

    node_chain = longest

if __name__ == "__main__":
    node_port = int(input("Port number? "))
    node.run(host='0.0.0.0', port=node_port)
