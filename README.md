How to simulate (needs many terminals):
python version: 3.x\n

<terminal 1 - server containing peer miner info>
$ python peers.py

<terminal 2 - miner at port 5000>
$ python miner.py
Port number? 5000

<terminal 3 - miner at port 5001>
$ python miner.py
Port number? 5001

<terminal 4>
$ ./tx.sh 5000 Alice Bob 50  // Alice sends 50 Coin to Bob through miner at port number 5000
$ ./mine.sh 5000  // miner at port 5000 mines its transactions\n
$ ./chain.sh 5000  // check the chain belongs to the miner at port 5000\n
$ ./chain.sh 5001  // check the chain belongs to the miner at port 5001\n
