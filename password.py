import random


def randomCharacter():
    randomInt = random.randint(33, 126)
    randomChar = (chr(randomInt))
    return randomChar

def generatePassword(n):
    password = ''
    for _ in range(int(n)):
      password += randomCharacter()
    return password


passwordLength = input('Please enter a length for the password: ')
print('Password: ' + generatePassword(passwordLength))

