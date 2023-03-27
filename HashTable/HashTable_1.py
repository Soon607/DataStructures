hash_table=list([0 for i in range(8)])

def get_key(data):
    return hash(data) # generate random numbers

def hash_function(key):
    return key%8

def save_data(data,value):
    hash_address=hash_function(get_key(data))
    hash_table[hash_address]=value
    
def read_data(data):
    hash_address=hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Steve','01012345678')
save_data('Jude','12345687')
print(read_data('Steve'))
print(hash_table)