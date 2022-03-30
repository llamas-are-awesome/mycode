import random
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))
number1 = chr(random.randint(48,57))
number2 = chr(random.randint(48,57))
punc1= chr(random.randint(33,46))
punc2= chr(random.randint(33,46))

passwd= uppercaseLetter1+ uppercaseLetter2+ lowercaseLetter1+ lowercaseLetter2+ number1+ number2+ punc1+ punc2
passwd= shuffle(passwd)
print(passwd)
