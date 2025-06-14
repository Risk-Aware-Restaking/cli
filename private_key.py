from eth_account import Account
import json
import os
import argparse

def generate_eth_account(name):
    # Enable account creation
    Account.enable_unaudited_hdwallet_features()
    
    # Generate a new account
    account = Account.create()
    
    # Get the private key and address
    private_key = account.key.hex()
    address = account.address
    
    # Create credentials dictionary
    credentials = {
        "name": name,
        "private_key": private_key,
        "address": address
    }
    
    # Create accounts directory if it doesn't exist
    os.makedirs("accounts", exist_ok=True)
    
    # Save credentials to JSON file
    json_path = f"accounts/{name}.json"
    with open(json_path, "w") as f:
        json.dump(credentials, f, indent=4)
    
    print("Ethereum account generated successfully!")
    print(f"Address: {address}")
    print(f"Credentials saved to: {json_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a new Ethereum account')
    parser.add_argument('name', help='Name for the account')
    args = parser.parse_args()
    
    generate_eth_account(args.name)
