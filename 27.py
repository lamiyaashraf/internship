username=input("enter the username:")
if username.isalnum() and 6<=len(username)<=15:
    print("valid username")
else:
    print("invalid username")
