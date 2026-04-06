import random as rd 
import string as st
letters = st.ascii_lowercase + st.ascii_uppercase + st.digits + "!@#$%^&*()_+-={}[]|\:;<>,.?/~"
digits = st.digits
size = len(letters) - 1
def generatePassword(length=20):
    global letters,size 
    # print(letters)
    password = []
    separator = ''
    for count in range(0,length):
        password.append(letters[rd.randint(0,size)])
    return separator.join(password)

def getotp(length=6):
    global digits
    size = 9 #local variable
    otp = []
    for count in range(0,length):
        otp.append(digits[rd.randint(0,size)])
    return ''.join(otp)    

print(generatePassword())
print(getotp())
# print(getotp(10))
# print(generatePassword(50))
# print(generatePassword(100))
