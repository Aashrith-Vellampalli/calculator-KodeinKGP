import math
import random
database={}

def generate_salt():
    salt=''
    for i in range(5):
        num=random.randint(0,26)
        probability=random.randint(0,1)
        if probability<=0.5:
            salt+=str(chr(65+num))
        else:
            salt+=str(num)
    return salt

def hash_password(password,salt):
    hash=''
    for i in salt+password:
        if i.isdigit():
            hash+=str(int(i)*3+2)
        elif i.isalpha():
            hash+=str(ord(i)*3+1)
        else:
            hash+=str(ord(i)*5+1)
    return hash
def register():
    username=input('Enter username: ')
    if username in database:
        print('User already exists')
        return
    password=input('Enter password: ')
    salt=generate_salt()
    hash=hash_password(password,salt)
    database[username]={'salt':salt,'hash':hash}
    print('User registered successfully')      

def login():
    username=input('Enter username: ')
    if username not in database:
        print('User does not exist')
        return
    password=input('Enter password: ')
    salt=database[username]['salt']
    hash=hash_password(password,salt)
    if hash==database[username]['hash']:
        print('Login successful')
    else:
        print('Login failed')

while True:
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    choice=input('Enter choice: ')
    if choice=='1':
        register()
    elif choice=='2':
        login()
    elif choice=='3':
        break
    else:
        print('Invalid choice')
        break
    