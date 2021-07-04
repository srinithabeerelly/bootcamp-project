import hashlib

mystring = input('Enter String to hash: ')

md5_value = hashlib.md5(mystring.encode())

print('The  md5 value is :', md5_value.hexdigest())
