"""

Copyright (C) 2017 Sai.
All Rights Reserved.

"""

# Shell command in Shell
# dir(int), dir(objectName)
# help(functionName)
test_int = 5
test_str = 'Today is Friday'

# Because tuple can't be changed, so the performance is better for fetching value!
# Normally using 【tuple】 to store a button or graphical interface that you won't modify it!
# Using square bracket to create LIST, List can be changed!
# Using normal bracket to create TUPLE, Tuple can't be changed!
test_list = ["Today", "DeleteME!", 3 , "Four"]
test_tuple = ("Today", "DeleteME!", 3 , "Four")

test_dictionary = {"Name":"Sai", "Profession":"Analyst"} # Using curly bracket

# Keep in mind everything we receive from input method is 'A STRING'!
userinput = input("Try to input a random number on python console?")
print(int(userinput) * 100)

# Python using indentation to define the block of function
# And those python-syntax inside that block should remain the same indentation level.
def c2fConverter(inputDegreeOfC):
    print('\n======Start of c2fConverter========')
    print(type(inputDegreeOfC))
    print(inputDegreeOfC.__class__.__name__)
    print(inputDegreeOfC*33.8)

def learnHow2SubString(inputSubString):
    print('\n======Start of Substring========')
    print(inputSubString[9:15]) # Which means get data from 9 to 14
    print(inputSubString[9:])
    print(inputSubString[-6:])
    print(inputSubString[-6:-3])
    # Return F because the first extra is 'Friday', then we extra it from right to left fro 6 digit again
    print(inputSubString[-6:][-6])

# List in Python is just like array in other languages
def learnListSystnax(inputList):
    print('\n=======Start of List Syntax=======')
    print(inputList)
    print(inputList[2:])
    print(inputList[1:2])
    print(inputList[-3])

def learnListMethod(inputList):
    print('\n=======Start of List Method======')
    print(type(inputList))
    print(len(inputList))
    print('-------Operating-------')
    print(inputList)
    del inputList[1]
    print(inputList)
    inputList.append("Tail")
    print(inputList)
    inputList.insert(1, "Reborn")
    print(inputList)
    inputList.remove("Reborn")  #If you dunno the index of List, you can use it's value to remove
    print(inputList)
def smallFunction(inputStr):
    return inputStr

def learnDictionary(inputDic):
    print('\n=======Start of Dictionary======')
    print(inputDic["Name"])
    dictionary_value = inputDic.values();  # Extract only value of dictionary
    dictionaryConvert2List = list(dictionary_value) # Convert Dictionary to List
    print(dictionary_value)


# Number and String
c2fConverter(test_int)
learnHow2SubString(test_str)

# List and Tuple
learnListSystnax(test_list)
learnListMethod(test_list)
try2AddFunctionToList = [smallFunction("Hello"), smallFunction("World")]
print(try2AddFunctionToList)

# Dictionary
learnDictionary(test_dictionary)


<<<<<<< HEAD:main.py



# Condition
userInput = 0
if userInput>0:
    print ("Greater")
elif userInput < 0:
    print("Lower")
else:
    print("Equal")

# Inline condition
print("Greater" if userInput>0 else "Lower")

# Since Python has not switch condition. The below example shows you replacements for switch statement in Python.
# Option 1:
def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]
# Option 2:
def f(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 9)    # 9 is default if x not found




#Looping
for email in testLooping_Emails:
    if 'gmail' in email: # Just like using SQL like syntax here!
        print(email)

#  We have a list with one item only. Therefore, the loop will iterate only once and print out that item.
a = ["Trickier"]
for i in a:
    print(i)

# Merging the same column as a list with different List
names = ['james', 'john', 'jack']
email_domain = ['gmail', 'hotmail', 'yahoo']
for i,j in zip(names, email_domain):
    print(i, j)


password = ''
while password != 'python123':
    password = input('Enter password: ')
    if password == 'python123':
        print("True")
    else:
        print ("False")


=======
>>>>>>> origin/master:dataType.py
