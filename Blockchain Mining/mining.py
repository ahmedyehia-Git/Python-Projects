# This program is bitcoin minning program with python 
# it is all about to create new hash that contain the block number
# the block contain information about the transactions that hapend in the this block plus the previous hash address
# the difficulties that now the bitcoin roles need that teh new hash should start with 20 zeros
# this make minning of new hash may take one year of computer processing on normal computer

from hashlib import sha256
import time

# This is example of how to ues hashlib library to print hexadiget 
#print(sha256("ABD".encode("ascii")).hexdigest())
#print(sha256("abc".encode("ascii")).hexdigest())
#print(sha256("ABD123".encode("ascii")).hexdigest())

# This variable will be used in loop to try different numbers till we get the hash with desirable criteria, one mill mean that the computer will try the number between 0 to 1000000, nonce is the gissing number that we will use to getthe hash
Max_nonce = 10000000000

# A function that can return hexadiget of any text
def SHA256(a): 
   return sha256(a.encode("ascii")).hexdigest()

# This is the main function of the program formining
# it should contain block number, transactions, previous hash, and we should feed the number of zeros in the prefix 

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0"*prefix_zeros
    for i in range (Max_nonce):
        a = str(block_number) + transactions + previous_hash + str(i)
        new_hash = SHA256(a)
        if new_hash.startswith(prefix_str):
            return new_hash     

    raise BaseException(f'Could not find a new hash after trying {Max_nonce} times')
    
# this function to calculate the time spent to generate new hash
#def time():


# this is the main function that start the program
if __name__=='__main__':
    transactions = '''
    Ahmed -> Reda ->20'
    Yara -> Yousra -> 40
    '''
    zeros = 6 # new hash will start with only 6 zeros
    
    # we start time to calculate the time consumed in miningprocess
    
    start = time.time()
    print('Start Mining')
    new_hash = mine(10, transactions, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', zeros)
    print(new_hash)
    total_time = str((time.time() - start))
    print(f"End mining. Mining took: {total_time} seconds")
    # in the above line we call the mine function and give it needed parameters, 
    # 10 is the block_number, 
    # transaction is the one that we add above    
    # we add dummy previous hash, 
    # and the number of zeros needed as prefix
