# Function to read balance from BankData.txt
def read_balance():
    try:
        with open("BankData.txt", "r") as file:
            balance = float(file.readline())
    except FileNotFoundError:
        # Create BankData.txt if it doesn't exist
        with open("BankData.txt", "w") as file:
            file.write("0.0")
        balance = 0.0
    return balance

# Function to write balance to BankData.txt
def write_balance(balance):
    with open("BankData.txt", "w") as file:
        file.write(str(balance))

# Function to log transactions to TransactionLog.txt
def log_transaction(transaction_type, amount):
    with open("TransactionLog.txt", "a") as file:
        file.write(f"{transaction_type}: {amount}\n")

# Function to make a deposit
def make_deposit():
    amount = float(input("How much would you like to deposit? "))
    if amount > 0:
        balance = read_balance()
        balance += amount
        write_balance(balance)
        log_transaction("Deposit", amount)
        print(f"Deposit of ${amount} successful.")
        print(f"Current balance: ${balance}")
    else:
        print("Invalid amount entered.")

# Function to make a withdrawal
def make_withdrawal():
    amount = float(input("How much would you like to withdraw? "))
    balance = read_balance()
    if 0 < amount <= balance:
        balance -= amount
        write_balance(balance)
        log_transaction("Withdrawal", amount)
        print(f"Withdrawal of ${amount} successful.")
        print(f"Current balance: ${balance}")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        print("Invalid amount entered.")

# Main function
def main():
    print("Welcome to the Bank Application!")
    while True:
        choice = input("Would you like to make a transaction? (Yes or No): ").lower()
        if choice == "no":
            break
        elif choice == "yes":
            balance = read_balance()
            print(f"Current balance: ${balance}")
            transaction_type = input("Would you like to make a deposit or withdrawal? (Deposit or Withdrawal): ").lower()
            if transaction_type == "deposit":
                make_deposit()
            elif transaction_type == "withdrawal":
                make_withdrawal()
            else:
                print("Invalid input.")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
