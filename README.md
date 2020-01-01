# Register-Login

I wrote this program in Python 3.7. It simulates a register and login process. When you are asked to
'Login or Register?' you can chose Login by entering 'Login'/'L'/'l' or Register by entering 'Register'/'R'/'r'. 
When you first start the program, there is not yet an account saved in the data dictionary (where Username:Password pairs
are stored in), so you need to first register. After you have sucessfully registered, you can login by using your just registered account. If you enter the credentials wrong, the program will prompt you to try again. After a successfull Login you are granted access. As I did not develop the program any further, you are returned to the starting menu. You can register as many accounts as you want. 
By entering the command 'data', the dictionary containing the account credentials are displayed.
During each register process, salt and pepper is added to the password before being hashed using SHA512. The finished value is then stored inside the dictionary (alongside it's username key)
