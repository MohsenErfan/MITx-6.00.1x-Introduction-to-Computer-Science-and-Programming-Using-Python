"""Now write a program that calculates the minimum fixed monthly payment
 needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does
not change each month, but instead is a constant amount
that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.
The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal"""
balance = 3329
annualInterestRate = 0.2
a = 10
epsilon = 0.1
balance_n = balance
while balance_n >= epsilon:
    balance_n = balance
    for i in range(12):
        Remainingbalance = balance_n - (a)
        balance_n = Remainingbalance + (annualInterestRate/12.0 )* Remainingbalance
        #print('Remaining balance: {:.2f}'.format(balance))
    a += 10

if balance_n <= epsilon:
        print('Lowest Payment: ',a-10)
