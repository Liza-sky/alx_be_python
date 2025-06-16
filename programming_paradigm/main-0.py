import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]

    if ':' in command_input:
        command, value = command_input.split(':')
        try:
            amount = float(value)
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)
    else:
        command = command_input
        amount = None

    if command == "deposit" and amount is not None:
      account.deposit(amount)
      print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("invalid command.")

if __name__ == "__main__":
    main()