while True:
   print('Who are you?')
   name = input()
   if name != 'Jonah':
      continue
   print('Hello,' + name + ' What is the password? (It is a horrible password.)')
   password = input()
   if password == 'password':
      break
      print('Access granted.')
   