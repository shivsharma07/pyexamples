balance = 4267
annualInterestRate = 0.2

#balance = 3329; annualInterestRate = 0.2; Lowest Payment: 310
#balance = 4773; annualInterestRate = 0.2; Lowest Payment: 440
#balance = 3926; annualInterestRate = 0.2; Lowest Payment: 360

#balance = 3454; annualInterestRate = 0.15; Lowest Payment: 310
#balance = 3448; annualInterestRate = 0.15; Lowest Payment: 310
#balance = 3292; annualInterestRate = 0.15; Lowest Payment: 300

#balance = 339;  annualInterestRate = 0.18; Lowest Payment: 40
#balance = 776;  annualInterestRate = 0.18; Lowest Payment: 80
#balance = 3896; annualInterestRate = 0.18; Lowest Payment: 360
#balance = 4509; annualInterestRate = 0.18; Lowest Payment: 410
#balance = 3758; annualInterestRate = 0.18; Lowest Payment: 340
#balance = 4267; annualInterestRate = 0.2; Lowest Payment: 390
#balance = 3665; annualInterestRate = 0.04; Lowest Payment: 320

monthlyInterestRate = round(annualInterestRate/12.0, 2)
epsilon = 10
monthlyUpdatedBalance = balance
i = 0
fixedAmount = epsilon
while (i < 12  and  monthlyUpdatedBalance > 0):
    unpaidBalance = round((monthlyUpdatedBalance - fixedAmount))
    monthlyUpdatedBalance = round((unpaidBalance + (monthlyInterestRate * unpaidBalance)))
    i += 1
    if i == 12 and monthlyUpdatedBalance != 0:     
        monthlyUpdatedBalance = balance
        fixedAmount += epsilon
        i = 0
    if ((monthlyUpdatedBalance / fixedAmount)) < 1:
        print 'here : '+str((monthlyUpdatedBalance / fixedAmount))
        break
print "i: "+str(i)
print "Lowest Payment: "+str(fixedAmount)