import time
from web3 import Web3

# Connection amin'ny Polygon
RPC_URL = "https://polygon-rpc.com" 
web3 = Web3(Web3.HTTPProvider(RPC_URL))

def monitor():
    print("--- Bot velona sy mandeha any USA (Render) ---")
    while True:
        try:
            if web3.is_connected():
                block_number = web3.eth.get_block('latest')['number']
                print(f"Mijery Block vaovao: {block_number}")
            time.sleep(30)
        except Exception as e:
            print(f"Olana kely: {e}")
            time.sleep(10)

if __name__ == "__main__":
    monitor()

