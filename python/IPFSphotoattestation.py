from ipfshttpclient import connect
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json

# Connect to your Ethereum node
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load your Ethereum contract ABI and address
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = json.loads('YOUR_CONTRACT_ABI_JSON')

# Connect to your contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Connect to IPFS
ipfs = connect('/ip4/127.0.0.1/tcp/5001/http')

# Function to upload photo to IPFS and get its hash
def upload_to_ipfs(file_path):
    with ipfs.add(file_path) as res:
        return res['Hash']

# Function to store IPFS hash in Ethereum contract
def store_hash_in_contract(ipfs_hash):
    # Your Ethereum account address which will interact with the contract
    account_address = 'YOUR_ACCOUNT_ADDRESS'

    # Unlock your Ethereum account
    web3.eth.default_account = account_address
    web3.personal.unlockAccount(account_address, 'YOUR_ACCOUNT_PASSWORD')

    # Call the smart contract function to store the IPFS hash
    tx_hash = contract.functions.storeHash(ipfs_hash).transact()
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print("Transaction receipt:", tx_receipt)

# Example usage
if __name__ == "__main__":
    file_path = 'path_to_your_photo.jpg'
    ipfs_hash = upload_to_ipfs(file_path)
    print("Uploaded photo to IPFS. Hash:", ipfs_hash)
    store_hash_in_contract(ipfs_hash)
