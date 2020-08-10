from math import ceil
from math import floor
from math import log
from sys import argv
from sys import exit

if len(argv) != 5:
    print("Incorrect parameters")
    exit()

if "type" not in argv[1]:
    print("Incorrect parameters")
    exit()
    
    
type = argv[1][7:]
principal = 0
payment = 0
periods = 0
interest = 0

n = -1
for i in argv:
    n += 1
    if n == 0:
        continue
    
    if "principal" in i:
        principal = int(argv[n].split("=")[1])
    elif "payment" in i:
        payment = int(argv[n].split("=")[1])
    elif "periods" in i:
        periods = int(argv[n].split("=")[1])
    elif "interest" in i:
        interest = float(argv[n].split("=")[1])
        monthly_interest = float(interest / 100 / 12)

if principal < 0 or payment < 0 or periods < 0 or interest < 0:
    print("Incorrect parameters")
    exit()


if type != "annuity" and type != "diff":
    print("Incorrect parameters")
    exit()

if type == "diff" and "payment" in argv:
    print("Incorrect parameters")
    exit()

if type == "annuity" and "principal" in argv and  "payment" in argv and "periods" in argv:
    print("Incorrect parameters")
    exit()


if type == "diff":
    
    sum_of_payments = 0
    for i in range(1, periods + 1):
        monthly_payment = ceil((principal / periods) + monthly_interest * (principal - (principal * (i - 1)) / periods))
        sum_of_payments += monthly_payment
        print("Month {}: paid out {}".format(i, monthly_payment))
    
    print("Overpayment = {}".format(sum_of_payments - principal))
    

elif type == "annuity":
    # liczymy kwote poczatkowa (principal)
    if principal == 0:
        principal = payment / ((monthly_interest * (1 + monthly_interest) ** periods) / ((1 + monthly_interest) ** periods - 1))
        print("Your credit principal = {}!".format(principal))
        
        sum_of_payments = payment * ceil(periods)
        print("Overpayment = {}".format(sum_of_payments - principal))
        
    # liczymy skladke (payment)
    elif payment == 0:
        payment = ceil(principal * (( monthly_interest * (1 + monthly_interest) ** periods ) / ((1 + monthly_interest) ** periods - 1)))
        sum_of_payments = payment * ceil(periods)
        print("Your annuity payment = {}!".format(payment))
        print("Overpayment = {}".format(sum_of_payments - principal))
        
    # liczymy liczbe miesiecy (periods)
    elif periods == 0:
        periods = log(payment / (payment - monthly_interest * principal), 1 + monthly_interest)
        no_of_years = floor(periods / 12)
        no_of_months = ceil(periods % 12)
        
        if no_of_months == 12:
            no_of_years = no_of_years + 1
            no_of_months = 0
        
        info = "You need "
        if no_of_years > 1:
            info += "{} years".format(no_of_years)
        elif no_of_years == 1:
            info += "{} year".format(no_of_years)
        
        if no_of_years > 0 and no_of_months > 0:
            info += " and "
        
        if no_of_months > 1:
            info += "{} months".format(no_of_months)
            
        elif no_of_months == 1:    
            info += "{} month".format(no_of_months)
        
        info += " to repay this credit!"
        
        print(info)
        
        sum_of_payments = payment * ceil(periods)
        print("Overpayment = {}".format(sum_of_payments - principal))
    
    



    



