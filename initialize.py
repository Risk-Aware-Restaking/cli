import json
import os

def register_network(network_name):
    private_key = json.load(open(f"accounts/{network_name}.json"))["private_key"]

    # Run python symb.py --chain sepolia register-network --private-key <private_key>
    os.system(f"python symb.py --chain sepolia register-network --private-key {private_key}")

def main():
    register_network("network1")

if __name__ == "__main__":
    main()