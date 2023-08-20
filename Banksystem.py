
print("="*20)

customerNames = ['Jane Smith', 'Iason Jordan', 'David Morgan', 'Brain John', 'Jack Swift' ]
customerPins = ['0123','2575','2312','7275','5049']
customerBalances = [1000, 2000, 30000, 40000, 5000]
deposition = 0 
withdrawal = 0 
balance = 0 
counter_1 = 1 
counter_2 = 5 
i = 0

#This statement below helps the program to run continuously.
while True:
    # os.system("cls")
    print("================================================")
    print(" -----Welcome to Times Bank-----       ")
    print("************************************************")
    print("=<< 1. Open a new account                    >>=")
    print("=<< 2. Deposite Money                        >>=")
    print("=<< 3. Withdraw Money                        >>=")
    print("=<< 4. Check Customers & Balance             >>=")
    print("=<< 5. Exit/Quit                             >>=")
    print("************************************************")
    
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
        print("choice number 1 is selected by the customer")
        # The line below will take the no:of customers from the user.
        NOC = eval(input("Number of Customers : "))
        i = i + NOC 
        # The if condition will restrict the number of new account of 5.
        if i > 5:
            print("\n")
            print("Customer registration exceed reached or customer registration too low : ")
            i = i - NOC 
        else:
            # The while loop will run according to the no:of customers.
            while counter_1 <= i:
                # These few lines will take information from customers.
                name = input("Input Fullname : ")
                customerNames.append(name)
                pin = str(input("Please input a pin of your choice : "))
                customerPins.append(pin)
                balance = 0 
                deposition = eval(input("Please input a value to deposite to start on account : "))
                balance = balance + deposition 
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter_2])
                print("Pin=", end=" ")
                print(customerPins[counter_2])
                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1 
                counter_2 = counter_2 + 1 
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is available on the customers list now :  ")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("======================================")
                # This statement below helps the user to go back to the  statement.
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit....")
    elif  choiceNumber == "2":
        j = 0 
        print("Choice number 2 is selected by the customer")
        # This while loop will prevent the user using the account if the username.
        while j < 1:
                k = -1 
                name = input("Please input name : ")
                pin = input("Please input pin : ")
                # This while loop will keep the function running when variabe k is smaller then length of the
                # customerNames list.
                while k < len(customerNames) - 1:
                    k = k + 1 
                    # These two if conditions find where both the name and pin matches.
                    if name == customerNames[k]:
                       if pin == customerPins[k]:
                            j = j + 1 
                            # These few statement would show the balance taken from the list.
                            print("Your Current Balance:", end=" ")
                            print(customerBalances[k], end=" ")
                            print("-/RS\n")
                            balanced = (customerBalances[k])
                            # Statement below would take the amount to withdraw from user.
                            withdrawal = eval(input("Input value to withdrawal : "))
                            # The if condition below would look whether the withdraw is greather than the balance.
                            if withdrawal > balance:
                               # This statement below would take a deposition from the customer.
                               deposition = eval(input("Please Deposite a higher value because your Balance menensioned above is not enough : "))
                               # These few statement would update the value and show the deposite taken from the list.
                               balance = balance + deposition 
                               print("Your Current Balance:", end=" ") 
                               print(balance, end=" ")
                               print("-/RS\n")
                               balance = balance - withdrawal 
                               print("-\n")
                               print("----Withdraw Successfull!----")
                               customerBalances[k] =  balance 
                               print("Your New Balance: ", balance, end=" ")
                               print("-/RS\n\n")
                            else:
                                # Else condition mensioned above is to do withdraw if the balance is greater than the
                                # withdraw amount.
                                balance = balance - withdrawal 
                                # These few statement would update the values in the list and show it to the customer.
                                print("\n")
                                print("-----Withdraw SUccessfull!------")
                                customerBalances[k] = balance 
                                print("Your New Balance:", balance, end=" ")
                                print("-/RS\n\n")
                if j < 1:
                    # The if condition above would work when the pin or the name is wrong.
                    print("Your name and pin does not match!\n")
                    break 
                # This statement below helps the user to go back to the start of the program.
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit....")
        
    elif  choiceNumber == "3":      
            print("Choice number 3 is selected by the customer")
            n = 0
            # The while loop below would work when the pin or the username.
            while n < 1:
                k = -1 
                name = input("Please input name : ")
                pin = input("Please input pin  : ")
                # The while loop below will keep the function running untill all the customer.
                while k < len(customerNames) - 1:
                    k = k + 1 
                    # The two if condition below would find whether.
                    if name == customerNames[k]:
                       if pin == customerPins[k]:
                            n = n + 1 
                            # These statement below would show the customer balance.
                            # The deposition made.
                            print("Your Current Balance: ", end=" ")
                            print(customerBalances[k], end=" ")
                            print("-/Rs")
                            balance = (customerBalances[k])
                            # This Statement below takes the deposition from customer.
                            deposition = eval(input("Enter the value you want to deposition : "))
                            balance = balance + deposition 
                            customerBalances[k] =  balance     
                            print("\n")
                            print("----Deposition Successfull!----")
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n") 
            if n < 1:
                print("Your name and pin does not match!\n")
                break 
                # This statement below helps the users to go back to the statement.
            mainMenu = input("Please press enter key to go back to main menu to perform another function or exit...")        
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0 
        print("Customer name list and balances mensioned below : ")
        print("\n")
        # The while loop below will keep the function running untill all the.
        while k <= len(customerNames) - 1:
            print("->.Customer = ", customerNames[k])
            print("->.Balance = ", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1 
            #This statement below helps the users to go back to the statement.
        mainMenu = input("Please press enter key to go back to main menu")   
    elif choiceNumber == "5":
        # This statement would be just showed to the customer.
        print("Choice number 5 is selected by the customer")  
        print("Thank you for using our banking system!")
        print("\n")
        print("Come Again")
        print("Bye bye")
        break
    else:
        #This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the Customer")
        print("Please try again!")
        #This statement below helps the users to go back to the start of the program .
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit...")



