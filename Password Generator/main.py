# In this program we will take input from user about the length of the password, 
# then we generate a random password and convert it to a hash for more security 

from random import choice
from hashlib import sha256

def pass_length():
    while True:
        try:
            len = int(input('Please enter the length of required password between 1 to 99: '))
        except ValueError:
            print('Invalid input!, Please enter valid number!')
            continue
            
        if  len <= 0 or len >99:                      
           print('Invalid password length! please try again.. ')
           continue
         
        else: 
            print(f'You select to have a password of {len} characters length!')
            break
      
    return int(len)   
# The above method is the stander one to validate user input 

# this function is to genrate random password 
def pass_generat():       
    password = ''
    char = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*<>?'

    for i in range(pass_length()):
        password += choice(char) 
        
    print(password)  
    return password 

def hash_generat():
        a = str(pass_generat())
        new_hash = sha256(a.encode("ascii")).hexdigest()
        print(new_hash)
        return new_hash  


def main():
    #pass_length()
    #pass_generat()
    hash_generat()
# as we define 'pass_length' within 'pass_generate' and the last one in 'hash_generat' 
# so all what we need is to run hash_generat() only

if __name__=='__main__':
    main()