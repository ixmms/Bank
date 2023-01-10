ClientNames = ['John Jacobs', 'Enzo Ferrari', 'Jeremy Davidson', 'Mohammed Abdulaziz', 'Carlos Envv', 'Ryan White', 'Conner Mark']
ClientPinNum = ['7100', '7101', '7103', '7104', '7105', '7106', '7107']
ClientFunds = [12000, 50500, 540052, 51060, 10000, 5000, 9510000]
ClientDeposit = 0
ClientWithdraw = 0
ClientBalance = 0
disk1 = 1
disk2 = 7
c = 0
while True:
    #Options List, user must select one of the options
    print("============================================================")
    print("==========     WELCOME TO XYZ BANKING SYSTEM    ============")
    print("============================================================")
    print("==========     (a). Open New Client Account     ============")
    print("==========     (b). Withdraw a Money            ============")
    print("==========     (c). Deposit Funds               ============")
    print("==========     (d). Check Clients & Balance     ============")
    print("==========     (e). Quit                        ============")
    print("============================================================")
    #When user selects one of the follwing options, such as option "a", the following will happen:
    UserInput = input("Select a Letter from the Above Box menu : ")
    if UserInput == "a":
        NumberOfClient = eval(input("Number of Clients : "))
        c = c + NumberOfClient

        if c > 7:
            print("\n")
            print("Client registration exceed reached or Client registration too low")
            c = c - NumberOfClient
        else:
            while disk1 <= c:
                name = input("Write Your Fullname : ")
                ClientNames.append(name)
                pin = str(input("Please Write a Pin number Consisted of Four Numbers only: "))
                ClientPinNum.append(pin)
                ClientBalance = 0
                ClientDeposit = eval(input("Please Insert Your Initial Deposit to Start an Account: "))
                ClientBalance = ClientBalance + ClientDeposit
                ClientFunds.append(ClientBalance)
                print("\nName=", end=" ")
                print(ClientNames[disk2])
                print("Pin=", end=" ")
                print(ClientPinNum[disk2])
                print("Balance=", "P", end=" ")
                print(ClientFunds[disk2], end=" ")
                disk1 = disk1 + 1
                disk2 = disk2 + 1
                print("\nYour name is added to the list of Clients")
                print("Your pin is added successfully")
                print("Your balance has been added successfully")
                print("----New account created successfully, Welcome to XYZ Bank!----")
                print("\n")
                print("Your Name is Available on the Client list now : ")
                print(ClientNames)
                print("\n")
                print("Note! Please remember the Name and Pin, if you forget your pin, you must call us on +4420123456 or visit our website www.XYZBank.com/PinServices")
                print("================================================================================================================================================")

        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif UserInput == "b":
        v = 0
        while v < 1:
            w = -1
            name = input("Please Insert b Client's Name : ")
            pin = input("Please Insert a Client's pin : ")
            while w < len(ClientNames) - 1:
                w = w + 1
                if name == ClientNames[w]:
                    if pin == ClientPinNum[w]:
                        v = v + 1
                        print("Your Current Balance:", "P", end=" ")
                        print(ClientFunds[w], end=" ")
                        print("\n")
                        ClientBalance = (ClientFunds[w])
                        ClientWithdraw = eval(input("Insert value to Withdraw : "))
                        if ClientWithdraw > ClientBalance:
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            ClientBalance = ClientBalance + deposition
                            print("Your Current Balance:", "P", end=" ")
                            print(ClientBalance, end=" ")
                            ClientBalance = ClientBalance - ClientWithdraw
                            print("-\n")
                            print("----Withdraw Successfully!----")
                            ClientFunds[w] = ClientBalance
                            print("Your New Balance: ", "P", ClientBalance, end=" ")
                            print("\n\n")
                        else:
                            ClientBalance = ClientBalance - ClientWithdraw
                            print("\n")
                            print("----Withdraw Successfully!----")
                            ClientFunds[w] = ClientBalance
                            print("Your New Balance: ", "P", ClientBalance, end=" ")
                            print("\n")
            if v < 1:
                print("Error! Your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
    elif UserInput == "c":
        x = 0
        while x < 1:
            w = -1
            name = input("Please Insert Your Name: ")
            pin = input("Please Insert Your Pin: ")
            while w < len(ClientNames) - 1:
                w = w + 1
                if name == ClientNames[w]:
                    if pin == ClientPinNum[w]:
                        x = x + 1
                        print("Your Current Balance: ", "P", end=" ")
                        print(ClientFunds[w], end=" ")
                        ClientBalance = (ClientFunds[w])
                        print("\n")
                        ClientDeposit = eval(input("Enter the value you want to deposit : "))
                        ClientBalance = ClientBalance + ClientDeposit
                        ClientFunds[w] = ClientBalance
                        print("\n")
                        print("----Transaction Successful!----")
                        print("Your New Balance: ", "P", ClientBalance, end=" ")
                        print("\n")
            if x < 1:
                print("ERROR, your name and pin does not match!\n")
                break
        mainMenu = input(" Press Enter Key to go Back to Main Menu or Quit_")
    elif UserInput == "d":
        w = 0
        print("Client name list and balances mentioned below : ")
        print("\n")
        while w <= len(ClientNames) - 1:
            print("->.Customer =", ClientNames[w])
            print("->.Balance =", "P", ClientFunds[w], end=" ")

            print("\n")
            w = w + 1
        mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
    elif UserInput == "e":
        print("Thank you for using our XYZ Bank!")
        print("\n")
        break
    else:
        print("Invalid option selected by the Client, Please Try again!")

        mainMenu = input("Press Press any Key to go Back to Main Menu or Quit_")
