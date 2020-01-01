import hashlib
d ={} #dictionary where key:value (username:password) pairs are stored in

def register(): #function called when you register
	usr = input("\nUsername: ") 
	psw = hashlib.sha512(("salt" + input("Password: ") + "pepper").encode()).hexdigest()
	if hashlib.sha512(("salt" + input("Retype Password: ") + "pepper").encode()).hexdigest() == str(psw): #password is hashed to increase security
		d.update({usr:psw}) #dictionary is updated with new account
		print("\nRegistration successfull!\n")
		return
	else:
		print("\nPasswords not the same, please try again.")
		register()
  	
def login(): #function called when you login
	usr = input("\nUsername: ")
	psw = input("Password:")
	if usr in d and hashlib.sha512(("salt" + str(psw) + "pepper").encode()).hexdigest() == d[usr]:
		print("Access granted!\n")
    
	else:
		print("\nAccount not found. \nPlease try again or register for free!\n")
		return
		
		
while True:
	print("Login or Register?")
	Inpt = input("")
	if Inpt== "Register" or Inpt=="r" or Inpt=="R":
		register()
		continue
	elif Inpt == "Login" or Inpt== "l" or Inpt=="L":
		login()
		continue
	elif Inpt== "data": 
		print(d)
		continue
	else:
		print("\nPlease enter a valid answer (Login/Register)")
		continue
  	

  


