total=0
def menu():
    while True:
        print("-----Menu-----")
        print(" 1 , pizza: 150")
        print(" 2 , burger: 50")
        print(" 3 , cake:450")
        print(" 4 , checkout and exit") 
        global total
        
        choice=int(input("enter your choice (1-4)"))
        if choice==1:
            qt=int(input("enter no of quantity :"))
            total+=qt*150
            print("pizza added")
        elif choice==2:
            qt=int(input("enter no of quantity :"))
            total+=qt*50
            print("burger added")
        elif choice==3:
            qt=int(input("enter no of quantity :"))
            total+=qt*450
            print("cake added")
        elif choice==4:
            print("exit,visit again !!!")
            break
        else:
            print("invalid choice !")
        print("total bill ",total)       
menu()