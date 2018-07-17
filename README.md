How to simulate (needs many terminals):\n
python version: 3.x\n

<terminal 1 - server containing peer miner info>\n
$ python peers.py

<terminal 2 - miner at port 5000>\n
$ python miner.py
Port number? 5000

<terminal 3 - miner at port 5001>\n
$ python miner.py
Port number? 5001

<terminal 4>\n
$ ./tx.sh 5000 Alice Bob 50  // Alice sends 50 Coin to Bob through miner at port number 5000\n
$ ./mine.sh 5000  // miner at port 5000 mines its transactions\n
$ ./chain.sh 5000  // check the chain belongs to the miner at port 5000\n
$ ./chain.sh 5001  // check the chain belongs to the miner at port 5001\n
