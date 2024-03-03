import itertools
import subprocess
import requests

def calculate_wallet_balance(seed_phrase):
    def generate_permutations(fixed_words, remaining_length):
        return itertools.product(fixed_words, repeat=remaining_length)

def main():
    # Take the fixed words as input
    fixed_words = input("Enter the 8 fixed words separated by space: ").split()

    # Ensure that there are exactly 8 fixed words
    if len(fixed_words) != 8:
        print("Please enter exactly 8 fixed words.")
        return

    # Take the remaining words for permutations
    remaining_words = input("Enter the remaining 16 words separated by space: ").split()

    # Ensure that there are exactly 16 remaining words
    if len(remaining_words) != 16:
        print("Please enter exactly 16 remaining words.")
        return

    # Generate all possible combinations for the remaining words
    all_permutations = generate_permutations(remaining_words, 16)

    # Iterate over all permutations and check the balance
    for permutation in all_permutations:
        seed_phrase = " ".join(fixed_words + list(permutation))
        balance = calculate_wallet_balance(seed_phrase)

        # Display the current seed phrase and balance
        print(f"Seed Phrase: {seed_phrase}\nWallet Balance: {balance} BTC\n")

        # Convert balance to USD (replace with the actual rate)
        balance_usd = balance * current_btc_to_usd_rate

        # Display balance in USD
        print(f"Balance in USD: {balance_usd} USD\n")

        # Decide when to stop (for demonstration purposes, it stops when balance is greater than 0.1 BTC)
        if balance > 0.1:
            print("Balance greater than 0.1 BTC found. Stopping.")
            break

if __name__ == "__main__":
    # Set the current BTC to USD rate (replace with the actual rate)
    current_btc_to_usd_rate = 40000  # Replace with the actual rate

    main()
