# This program says hello and asks for my name

print('Hello world')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

# Asks for age
print('What is your age?')
myAge = input()
print('You will be' + str(int(myAge) + 1) + 'in a year.')