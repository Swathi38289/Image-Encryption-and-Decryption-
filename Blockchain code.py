from web3 import Web3

# Connect to Ganache
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Contract details
contract_address = "0xF64aDc001BBef00CF32753799469c423A1358FDE"
abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "imageId",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "encryptedKey",
                "type": "string"
            }
        ],
        "name": "AccessGranted",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "imageId",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "string",
                "name": "newEncryptedKey",
                "type": "string"
            }
        ],
        "name": "grantAccess",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "imageId",
                "type": "uint256"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "ipfsHash",
                "type": "string"
            }
        ],
        "name": "ImageUploaded",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "ipfsHash",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "encryptedKey",
                "type": "string"
            }
        ],
        "name": "uploadImage",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "imageId",
                "type": "uint256"
            }
        ],
        "name": "getImage",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = web3.eth.contract(address=contract_address, abi=abi)

# Account details
account = "0x5eb8475383CC1595Ef2eDce1acD8395f6F101f28"
private_key = "30bb6e9ccaeb13b6f6499c5b17cc87e693fdc86fe8efb5628494b07ea35ad1b3"

# Record image hash on blockchain
def record_image(image_hash, encrypted_key):
    nonce = web3.eth.get_transaction_count(account)
    txn = contract.functions.uploadImage(image_hash, encrypted_key).build_transaction({
        'chainId': 1337,
        'gas': 3000000,
        'gasPrice': web3.to_wei('20', 'gwei'),
        'nonce': nonce
    })
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    print(f"Transaction sent: {web3.to_hex(tx_hash)}")

# Call the function with appropriate parameters
record_image("image_hash_placeholder", "encrypted_key_placeholder")

