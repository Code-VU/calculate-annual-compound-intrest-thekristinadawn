def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you

    client_one_principal = float(input("Principle (amount): "))
    client_one_time =float(input("Time:               "))
    client_one_rate =float(input("Rate:               "))
    client_two_principal = float(input("Principle (amount): "))
    client_two_time =float(input("Time:               "))
    client_two_rate =float(input("Rate:               "))
    client_three_principal = float(input("Principle (amount): "))
    client_three_time =float(input("Time:               "))
    client_three_rate =float(input("Rate:               "))
    
    #Calculates Compound Interest
    client_one_amount = client_one_principal*(pow((1+client_one_rate / 100), client_one_time))
    client_one_CI = round(client_one_amount - client_one_principal,2)
    client_two_amount = client_two_principal*(pow((1+client_two_rate / 100), client_two_time))
    client_two_CI = round(client_two_amount - client_two_principal,2)
    client_three_amount = client_three_principal*(pow((1+client_three_rate / 100), client_three_time))
    client_three_CI = round(client_three_amount - client_three_principal,2
                           )


    
    print("Principle (amount):",str(client_one_principal))
    print("Time:",str(client_one_time))
    print("Rate:",str(client_one_rate))
    print("Compound Interest:",str(client_one_CI))
    print("---")
    print("Principle (amount):",round(client_two_principal))
    print("Time:",(client_two_time))
    print("Rate:",(client_two_rate))
    print("Compound Interest:",client_two_CI)
    print("---")
    print("Principle (amount):",round(client_three_principal))
    print("Time:",(client_three_time))
    print("Rate:",client_three_rate)
    print("Compound Interest:",client_three_CI)
 #print("Compound Interest: "+str(intrest))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

#calculateCompoundInterest()
