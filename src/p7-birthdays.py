birthdays = {'Jonah': 'March 27, 2012', 'Noah': 'November 23, 2015', 'Appa': 'March 16, 1975', 'Mama': 'September 19,1978'}

while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break
        
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')