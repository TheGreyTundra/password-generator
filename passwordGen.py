from string import ascii_letters, punctuation
import random

#26 lowercase 26 uppercase 32 punctuation -  84
allPunc = punctuation
allCaps = ascii_letters[26:]
allLower = ascii_letters[:26]
allChars = ascii_letters + punctuation



gen = True
punct = False
upperCase = False


while gen:
    punct = False
    upperCase = False
    password = ""
    print("\n")
    punc = input("Do you need/want special characters?(Y/N): ")
    
    if punc == "Y":
        punct = True
       

    upper = input("Do you need atleast one Uppercase?(Y/N): ")

    if (upper == "Y"):
        upperCase = True
   

    charCount = int(input("Enter prefered amount of characters\nPress 0 to quit: "))

    if (charCount < 0):
        charCount = int(input("The entered number was less than zero please pick a positive int\nPress 0 to quit: "))

    elif (charCount == 0):
        gen = False
        break

    if (punct | upperCase):
        if (punct & upperCase):
            for i in range(charCount):
                random.randint(0,83)
                password += allChars[random.randint(0,83)]
                #print(password)
                

        elif (punct):
            Letters = ascii_letters[:26] +punctuation
            for i in range(charCount):
                password += Letters[random.randint(0,57)]
                #print(password)

        elif(upperCase):
            Letters = ascii_letters
            for i in range(charCount):
                password += ascii_letters[random.randint(0,51)]
                #print(password)
    else:
        for i in range(charCount):
            password += allLower[random.randint(0,25)]
            #print(password)

    print("\n\t"+password +"\n")



    




