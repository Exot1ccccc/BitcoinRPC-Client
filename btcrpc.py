from ast import Dict
from json import decoder
import pprint
from sre_constants import BRANCH
from bitcoinrpc.authproxy import AuthServiceProxy
from dotenv import load_dotenv
import os



class bitcoinrpcclient:
    def __init__(self):
        load_dotenv()
        rpc_user = os.getenv("rpc_user")
        rpc_pass = os.getenv("rpc_pass")
        rpc_host = os.getenv("rpc_host")
        self.rpc_client = AuthServiceProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:8332", timeout=120)  
         
        print(self.rpc_client)
         
    def rpc_call(self):       
        block_count = self.rpc_client.getblockcount()
        print("---------------------------------------------------------------")
        print("Block Count:", block_count)
        print("---------------------------------------------------------------\n")
    
    

    def rpc_arugements(self, block_count):      
        blockhash = self.rpc_client.getblockhash(block_count)
        block = self.rpc_client.getblock(blockhash)
        nTx = block['nTx']
        if nTx > 10:
            it_txs = 10
            list_tx_heading = "First 10 transactions: "
        else:
            it_txs = nTx
            list_tx_heading = f"All the {it_txs} transactions: "
        print("---------------------------------------------------------------")
        print("BLOCK: ", block_count)
        print("-------------")
        print("Block Hash...: ", blockhash)
        print("Merkle Root..: ", block['merkleroot'])
        print("Block Size...: ", block['size'])
        print("Block Weight.: ", block['weight'])
        print("Nonce........: ", block['nonce'])
        print("Difficulty...: ", block['difficulty'])
        print("Number of Tx.: ", nTx)
        print(list_tx_heading)
        print("---------------------")
        i = 0
        while i < it_txs:
            print(i, ":", block['tx'][i])
            i += 1
        print("---------------------------------------------------------------\n")

    def wallet_info(self):
        wallet_info = self.rpc_client.getwalletinfo()
        print("---------------------------------------------------------------")
        print("Wallet Info:")
        print("-----------")
        pprint(wallet_info)
        print("---------------------------------------------------------------\n")
    def list(self):
        tx_list = self.rpc_client.listtransactions()
        pprint(tx_list)

        print("Exploring UTXOs")
        ## List UTXOs
        utxos = self.rpc_client.listunspent()
        print("Utxos: ")
        print("-----")
        pprint(utxos)
        print("------------------------------------------\n")
        

