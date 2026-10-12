This README is made with AI

🏦 Python Bank Account Program
A simple command-line banking application built with Python. This program simulates a basic bank account, allowing users to deposit money, withdraw money, and check their balance — all through an easy-to-use text menu. It's a great beginner project for learning about object-oriented programming (OOP), classes, and user input handling in Python.

📖 Python Bank Account Program
The Python Bank Account Program is a console-based application that models a real-world bank account using a Python class. When the program starts, the user is prompted to enter the account owner's name. From there, a looping menu appears with options to deposit, withdraw, check the balance, or exit.

Each transaction is validated to prevent common errors — for example, the program refuses deposits or withdrawals of zero or negative amounts, and it blocks withdrawals that exceed the available balance. All user input for amounts is wrapped in error handling so that invalid (non-numeric) entries don't crash the program.

This project is ideal for anyone learning the fundamentals of Python classes, methods, and interactive programs.

✨ Features
Create an account with a custom owner name – Entered at startup.

Deposit money – Adds a positive amount to the account balance.

Withdraw money – Subtracts money, but only if sufficient funds exist.

Check balance – Displays the current balance along with the account owner's name.

Input validation – Rejects non-positive deposit/withdrawal amounts.

Overdraft protection – Prevents withdrawing more than the current balance.

Non-numeric input handling – Uses try/except to catch invalid number entries.

Looping menu – Keeps running until the user chooses to exit.

Simple exit option – Quit the program cleanly at any time.

🛠️ What It Uses
Language & Library
Python 3 – No external libraries required (pure standard library).

Class: BankAccount
Method	Purpose
__init__(self, owner, balance=0)	Initializes the account with an owner name and optional starting balance (defaults to 0).
deposit(self, amount)	Adds a positive amount to the balance. Rejects zero or negative values.
withdraw(self, amount)	Subtracts money if the balance is sufficient. Rejects invalid or excessive amounts.
check_balance(self)	Prints the owner's name and current balance.
Attributes
owner – The name of the account holder.

balance – The current amount of money in the account.

Python Concepts Demonstrated
Object-oriented programming – Defining and using a class.

Methods and attributes – Encapsulating behavior and data.

Conditional logic – Checking for valid amounts and sufficient funds.

Exception handling – try/except blocks for safe numeric input.

Loops – while True loops for the menu and input validation.

F-strings – Formatted output for messages and balances.

User input – Reading and processing input via input().

Built-in Functions Used
input() – Reads user input from the console.

float() – Converts string input into a number.

print() – Displays messages and menus.

exit() – Terminates the program.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
bank_account.py
No installation or dependencies are needed — just Python.

▶️ How to Run
Make sure you have Python 3 installed (python.org).

Save the code as bank_account.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python bank_account.py
Enter the account owner's name when prompted, then use the menu to deposit, withdraw, check your balance, or exit.
