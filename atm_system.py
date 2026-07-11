# ATM System Project with File Handling (JSON)

import json
import os

DATA_FILE = "atm_data.json"

# ---------- File Handling Functions ----------

def load_data():
    """Load balance, pin, transactions from file. If not present, create default."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {
            "balance": 5000,
            "pin": "1234",
            "transactions": []
        }
        save_data(data)
    return data

def save_data(data):
    """Save current data back to file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- ATM Functions ----------

def check_pin(data):
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == data["pin"]:
            print("PIN Verified Successfully!\n")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN. Attempts left: {attempts}")
    print("Account Blocked! Contact bank.")
    return False

def check_balance(data):
    print(f"Your current balance: Rs.{data['balance']}")

def withdraw_money(data):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Enter valid amount")
    elif amount > data["balance"]:
        print("Insufficient balance!")
    elif amount % 100 != 0:
        print("Amount should be in multiples of 100")
    else:
        data["balance"] -= amount
        data["transactions"].append(f"Withdrew Rs.{amount}")
        save_data(data)
        print(f"Withdrawal successful! Remaining balance: Rs.{data['balance']}")

def deposit_money(data):
    amount = int(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Enter valid amount")
    else:
        data["balance"] += amount
        data["transactions"].append(f"Deposited Rs.{amount}")
        save_data(data)
        print(f"Deposit successful! New balance: Rs.{data['balance']}")

def mini_statement(data):
    if len(data["transactions"]) == 0:
        print("No transactions yet")
    else:
        print("---- Mini Statement ----")
        for t in data["transactions"]:
            print(t)

def change_pin(data):
    old_pin = input("Enter old PIN: ")
    if old_pin == data["pin"]:
        new_pin = input("Enter new PIN: ")
        data["pin"] = new_pin
        save_data(data)
        print("PIN changed successfully!")
    else:
        print("Old PIN incorrect")

def main_menu(data):
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            check_balance(data)
        elif choice == "2":
            withdraw_money(data)
        elif choice == "3":
            deposit_money(data)
        elif choice == "4":
            mini_statement(data)
        elif choice == "5":
            change_pin(data)
        elif choice == "6":
            print("Thank you for using ATM. Visit again!")
            break
        else:
            print("Invalid choice! Try again.")

# ---------- Program Start ----------

print("===== WELCOME TO PYTHON ATM =====")
data = load_data()

if check_pin(data):
    main_menu(data)
