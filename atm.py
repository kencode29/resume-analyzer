def atm():
    balance=50000
    while True:
        print("------ATM------\n")
        print("1 for balance check")
        print("2 for deposite")
        print("3 for withdraw the cash")
        print("4 for exit from atm machine")

        b=int(input("entre your choice from (1-4) :"))
        if b==1:
            print(balance)
        elif b==2:
            n=int(input("enter the amount for deposite :"))
            if n>0:
                balance+=n
                print("Deposite succesfully",n)
            else:
                print("invalid amount !")
        elif b==3:
            n=float(input("enter the amount for withdraw "))
            if n<=0:
                print("invalid amount! enter a positive no. ")
            elif n>balance:
                print("insufficient balance !")
            else:
                balance-=n
                print("withdrawl successfully !")                 
        elif b==4:
            print("exit")
            break
        else :
            print("invalid number !")
            
atm()
            
            
        
        
              
        
        