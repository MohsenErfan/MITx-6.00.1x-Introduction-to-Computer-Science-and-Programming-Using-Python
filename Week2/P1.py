"""Write a program to calculate the credit card balance after
one year if a person only pays the minimum monthly payment
required by the credit card company each month.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
for i in range(12):
    Remainingbalance = balance - (monthlyPaymentRate*balance)
    balance = Remainingbalance + (annualInterestRate/12.0 )* Remainingbalance
print('Remaining balance: {:.2f}'.format(balance))
