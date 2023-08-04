import hashlib
from electrum.mnemonic import Mnemonic
from electrum.wallet import Standard_Wallet
from electrum.simple_config import SimpleConfig
from electrum import constants
from electrum.network import Network
from itertools import permutations

def check_wallet_balance(seed_phrase):
    seed = Mnemonic.to_seed(seed_phrase)
    master_private_key = hashlib.bip32_master_key(seed)
    wallet = Standard_Wallet.from_master_key(master_private_key)
    
    # Connect to Electrum network for balance retrieval
    config = SimpleConfig({'testnet': False})  # Adjust 'testnet' parameter if needed
    constants.set_config(config)
    network = Network(config)
    network.start()

    try:
        balance = wallet.get_balance()
        confirmed_balance, unconfirmed_balance = balance
        print("Seed phrase:", seed_phrase)
        print("Master private key:", master_private_key)
        print("Wallet address:", wallet.get_receiving_address())
        print("Confirmed balance:", confirmed_balance)
        print("Unconfirmed balance:", unconfirmed_balance)
        print("----------------------")
    finally:
        network.stop()

seed_phrase = "your seed phrase here"
permutations = permutations(seed_phrase.split())

for permutation in permutations:
    check_wallet_balance(' '.join(permutation))
