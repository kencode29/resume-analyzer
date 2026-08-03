users={
    "lio":"nik",
    "boom":"rdx",
    "jiwoo":"ray",
    "john":"vio"
}

username = input("enter your username :")
pas= input("enter your password :")

if username in users and users[username]==pas:
    print("login successfully !!!")
else:
    print("login failed !! ")
