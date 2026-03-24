import sys
from kyc import *

def createKYCReport():

    name = input("Enter name: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    data = {
        "name": name,
        "email": email,
        "address": address
    }

    json_data = convertDataToJSON(data)

    ipfs_hash = pinJSONtoIPFS(json_data)

    print("IPFS Hash:", ipfs_hash)

    web3, contract = initContract()

    account = web3.eth.accounts[0]

    tx = contract.functions.registerKYC(
        account,
        ipfs_hash
    ).transact({'from': account})

    print("Transaction successful:", tx)


def main():

    if len(sys.argv) < 2:
        print("Usage: python kycreport.py report")
        return

    if sys.argv[1] == "report":
        createKYCReport()


if __name__ == "__main__":
    main()