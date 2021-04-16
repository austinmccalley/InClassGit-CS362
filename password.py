import random


def randomCharacter():
    randomInt = random.randint(0, 255)
    randomChar = (chr(randomInt))
    return randomChar

def generatePassword(n):
    password = ''
    for _ in range(n):
      password += randomCharacter()


passwordLength = input('Please enter a length for the password: ')


