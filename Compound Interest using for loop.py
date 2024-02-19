def compound_interest(principal, rate, time):
    Amount = principal
    for i in range(time):
        Amount = Amount * (1 + rate/100)
    CI = Amount - principal
    print("Compound interest is", CI)
# Driver Code
compound_interest(1200, 5.4, 2)
