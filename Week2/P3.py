"""Write a program that uses these bounds and bisection search
(for more info check out the Wikipedia page on bisection search)
to find the smallest monthly payment to the cent (no more multiples of $10)
such that we can pay off the debt within a year. Try it out with large inputs,
and notice how fast it is (try the same large inputs in your solution to
Problem 2 to compare!).
Produce the same return value as you did in Problem 2."""

balance = 320000
annualInterestRate = 0.2
lower = balance/12
upper = (balance*(1+annualInterestRate/12)**12)/12
a = (upper+lower)/2
epsilon = 0.01
balance_n = balance
while abs(balance_n) >= epsilon:
    balance_n = balance
    for i in range(12):
        Remainingbalance = balance_n - (a)
        balance_n = Remainingbalance + (annualInterestRate/12.0 )* Remainingbalance
    if balance_n > 0:
        lower = (upper+lower)/2
    elif balance_n <0:
        upper = (upper+lower)/2
    a = (lower + upper) / 2


if balance_n <= epsilon:
        print('Lowest Payment: {:.2f}'.format(a))
