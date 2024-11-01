"""Import the Account class from the Account.py file."""
# savings_account.py

from account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # # account.py

class Account:
    def __init__(self, balance=0.0, interest_rate=0.0):
        self.balance = balance
        self.interest_rate = interest_rate  # Store the interest rate as a percentage

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def calculate_interest(self):
        # Calculate interest based on balance and interest rate
        return self.balance * (self.interest_rate / 100)


    # Calculate interest earned
     # def calculate_interest(self):
        # Calculate interest based on balance and interest rate
        return self.balance * (self.interest_rate / 100)


    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
