#balance = 5000
#annualInterestRate = 0.18
#monthlyPaymentRate = 0.02
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0
monthlyUpdatedBalance = balance
i = 0
totalPaid = 0.0
while i != 12:
    minimumMonthlyPayment = monthlyPaymentRate * monthlyUpdatedBalance
    monthlyUnpaidBalance = monthlyUpdatedBalance - minimumMonthlyPayment
    monthlyUpdatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    totalPaid += minimumMonthlyPayment
    print "Month: "+str(i+1)
    print "Minimum monthly payment: "+str(round(minimumMonthlyPayment,2))
    print "Remaining balance: "+str(round(monthlyUpdatedBalance,2))
    i += 1
print "Total paid: "+str(round(totalPaid,2))
print "Remaining balance: "+str(round(monthlyUpdatedBalance,2))