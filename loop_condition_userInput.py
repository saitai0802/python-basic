testLooping_Emails = ["me@gmail.com", "you@yahoo.com", "we@gmail.com"]

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


