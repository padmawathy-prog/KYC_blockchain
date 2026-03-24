import json
import requests
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")
WEB3_PROVIDER_URI = os.getenv("WEB3_PROVIDER_URI")
SMART_CONTRACT_ADDRESS = os.getenv("SMART_CONTRACT_ADDRESS")

def initContract():
    web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))

    with open("kyc.json") as f:
        contract_abi = json.load(f)

    contract = web3.eth.contract(
        address=SMART_CONTRACT_ADDRESS,
        abi=contract_abi
    )

    return web3, contract


def convertDataToJSON(data):
    return json.dumps(data)


def pinJSONtoIPFS(json_data):

    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }

    response = requests.post(
        url,
        data=json_data,
        headers=headers
    )

    ipfs_hash = response.json()["IpfsHash"]

    return ipfs_hash