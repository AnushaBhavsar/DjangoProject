userlist=[]
print("User Login")
print('''1. Sign in for new user
        2. Login for existing user
        3. Delete user
        4. Show all the users
        5. Exit''')

ch=0
while (ch != 5):
    ch=int(input("Enter your choice : "))
    if ch==1:
        user={}
        user['username']=input("Username : ")
        user['password']=input("Password : ")
        userlist.append(user)

    if ch==2:
        print("Login for existing user")
        for user in userlist:
            username=input("Enter your Username : ")
            password=input("Enter your Password : ")
            if user['username']==username and user['password']==password:
                print("Login successful")
                break
            else:
                print("Invalid Username or Password")
                break

    if ch==3:
        print("Delete user")
        for user in userlist:
            username=input("Enter the username : ")
            password=input("Enter the password : ")
            if user['username']==username and user['password']==password:
                del user['username']
                del user['password']
                print("User deleted successfully")
                break
            else:
                print("Invalid username")
                break

    if ch==4:
        print("Show all the users")
        for user in userlist:
            print (user)
            break
