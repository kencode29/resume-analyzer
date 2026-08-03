import random
numbers=list(range(11,46,4))
lucky_num=random.randrange(11,46,4)
print("numbers: ",numbers)
print("lucky number: ",lucky_num)
user_num=int(input("choose number :"))
bet=int(input("enter your bet amount :"))
if bet>50000:
    if user_num==lucky_num:
        numbers.remove(user_num)
        lucky_num=random.choice(numbers)
        print("lucky number is :",lucky_num)
    else:
        print("try next time ")
else:
    if lucky_num!=user_num:
        print("try again later ")
    else:
        print("you win: ",lucky_num,"is correct number")