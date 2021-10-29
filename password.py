import getpass

my_pass=getpass.getpass(prompt="Enter your password: ")

# To verify the password
#print("Entered password is:", my_pass)

user=getpass.getuser()
print("Current user logged in is:", user)