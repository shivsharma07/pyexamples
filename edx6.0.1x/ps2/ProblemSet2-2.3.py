balance = 776
annualInterestRate = 0.18

monthlyPayment = 10
monthlyInterestRate = annualInterestRate /12
newbalance = balance - 10

while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 0

    while month < 12 and newbalance > 0:
        newbalance -= monthlyPayment
        interest = monthlyInterestRate * newbalance
        newbalance += interest
        month += 1
    newbalance = round(newbalance,2)
print " Lowest Payment:", monthlyPayment