#!/usr/bin/python
# Probably don't need these imports:
#import os
#import socket
#import re
#import glob
#import time
#import math
#import subprocess
#import time
balance = 60000
annualInterestRate = .185
months = 12
print "Balance:", balance
print "Rate:", annualInterestRate
print "Months:", months
monthlyInterestRate = annualInterestRate/12
lowerBound = balance/months
upperBound = (balance * (1+annualInterestRate/12)**12)/months
originalBalance = balance

# Keep testing new payment values
# until the balance is +/- $0.02

while abs(balance) > .02:
# Reset the value of balance to its original value
    balance = originalBalance
 
# Calculate a new monthly payment value from the bounds
    payment = (upperBound - lowerBound)/2 + lowerBound

# Test if this payment value is sufficient to pay off the
# entire balance in x months
    for month in range(months):
        balance -= payment
        balance *= 1+monthlyInterestRate

# Reset bounds based on the final value of balance
    if balance > 0:
# If the balance is too big, need higher payment
# so we increase the lower bound
        lowerBound = payment
    else:
# If the balance is too small, we need a lower
# payment, so we decrease the upper bound
        upperBound = payment

# When the while loop terminates, we know we have our answer!
print "Lowest Payment:", round(payment, 2)

# Todo: figure out why >24 months does not work and fix that
# Todo: put in prompts to allow entering balance, rate, months
