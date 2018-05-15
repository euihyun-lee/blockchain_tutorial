from flask import Flask
from flask import request
import json
node = Flask(__name__)

peer_nodes = []

@node.route('/get_peers', methods = ['POST'])
def getPeer():
    new_node = request.get_json()
    print(new_node)
    if new_node['miner']:
        peer_nodes.append(new_node['url'])

    print(json.dumps(peer_nodes))
    return json.dumps(peer_nodes)

if __name__ == '__main__':
    node.run(host='0.0.0.0', port=8080)