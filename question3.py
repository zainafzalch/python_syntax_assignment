#Task 1: Grocery Store Math Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!

bread = 10
jelly = 5
peanut_butter = 1

print(bread + jelly + peanut_butter)

#Task 2: Bank Interest If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

balance = input("Enter account balance = ")
interest = input("Enter interest rate = ")
#interest = int(interest) / 100

def balanceAfterInterest(account_balance, interest_rate):
    return (float(account_balance) * (float(interest_rate) / 100)) + float(account_balance)

print(balanceAfterInterest(balance, interest))