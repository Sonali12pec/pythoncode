import re
# TODO: use getpass instead of input(), it does not echo the typed password
# https://docs.python.org/2/library/getpass.html
p= input("Input your password")

# TODO: It would have been better to create a separate function for password validation
x = True
while x:  
    # TODO: Read about re.compile and re.match 
    if (len(p)<6):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[*$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    # TODO: Why not valid. Give reason to user. Would help him to enter a valid one on next try
    print("Not a Valid Password")
