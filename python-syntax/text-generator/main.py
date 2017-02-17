import string, random

vowels_list = "aeiou"
consonants_list = "bcdfghjklmnpqrstvwxyz"
letter_list = string.ascii_lowercase

userInput_sr = ""
userInput_list = []
generatedName_list = []

def generate(userInput):

    userInput = userInput.lower()
    letter = ""
    if userInput == "v":
        letter = random.choice(vowels_list)
    elif userInput == "c":
        letter = random.choice(consonants_list)
    elif userInput == "l":
        letter = random.choice(string.ascii_lowercase)
    return letter

def createTenNames (userInput_list):
    for i in range(10):
        generatedName_str = ""
        for userInput in userInput_list:
            generatedName_str += generate(userInput)

        generatedName_list.append(generatedName_str.title())

while userInput_sr != 'create':
    print('What letter do you wan? Enter \'v\' for vowels, \'c\' for consonants, \'l\' for any letter. Other letter will be ignored')
    userInput_sr = input('Enter \'create \'to generate ten letter : ')
    userInput_sr = userInput_sr.lower()

    if userInput_sr == 'create':
        print("=============End==============")
        createTenNames(userInput_list)
        print(generatedName_list)
    else:
        userInput_list.append(userInput_sr)

    print("----------------------------------")