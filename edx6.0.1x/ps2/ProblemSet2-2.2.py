balance = 3926
annualInterestRate = 0.2

#balance = 3329; annualInterestRate = 0.2; Lowest Payment: 310
#balance = 4773; annualInterestRate = 0.2; Lowest Payment: 440
#balance = 3926; annualInterestRate = 0.2; Lowest Payment: 360

#balance = 3454; annualInterestRate = 0.15; Lowest Payment: 310 
#balance = 3448; annualInterestRate = 0.15; Lowest Payment: 310 x
#balance = 3292; annualInterestRate = 0.15; Lowest Payment: 300

#balance = 339;  annualInterestRate = 0.18; Lowest Payment: 40
#balance = 776;  annualInterestRate = 0.18; Lowest Payment: 80
#balance = 3896; annualInterestRate = 0.18; Lowest Payment: 360
#balance = 4509; annualInterestRate = 0.18; Lowest Payment: 410
#balance = 3758; annualInterestRate = 0.18; Lowest Payment: 340
#balance = 4267; annualInterestRate = 0.2; Lowest Payment: 390
#balance = 3665; annualInterestRate = 0.04; Lowest Payment: 320

monthlyInterestRate = annualInterestRate/12.0
epsilon = 10
monthlyUpdatedBalance = balance
fixedAmount = epsilon
while monthlyUpdatedBalance > 0:
    fixedAmount += epsilon
    monthlyUpdatedBalance = balance
    month = 0
    while (month < 12  and monthlyUpdatedBalance > 0):
        unpaidBalance = monthlyUpdatedBalance - fixedAmount
        monthlyUpdatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    monthlyUpdatedBalance = round(monthlyUpdatedBalance,2)
print "Lowest Payment: "+str(fixedAmount)