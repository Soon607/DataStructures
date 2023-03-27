# creating HashTable
hash_table=list([i for i in range(10)])

# creating HashFunction
def hash_func(key):
    return key%5

# storing data
data1='Andy'
data2='Dave'
data3='Trump'
data4='Anthor'

def storage_data(data,value):
    key=ord(data[0]) # return ASCII code
    hash_address=hash_func(key)
    hash_table[hash_address]=value
    

storage_data(data1,'01055553333')
storage_data(data2,'01044443333')
storage_data(data3,'01022223333')

def get_data(data):
    key=ord(data[0])
    hash_address=hash_func(key)
    return hash_table[hash_address]
