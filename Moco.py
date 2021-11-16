#Importing the libraries
import random
from random_username.generate import generate_username
import os

#Making a clear funtion
def clear():
    command = 'cls'
    if os.name != 'nt':
    	command = 'clear'
    os.system(command)
    return 0

#Clearing the console before begining
clear()

#Making a title variable for later on
title = ''' __    __     ______     ______     ______    
/\ "-./  \   /\  __ \   /\  ___\   /\  __ \   
\ \ \-./\ \  \ \ \/\ \  \ \ \____  \ \ \/\ \  
 \ \_\ \ \_\  \ \_____\  \ \_____\  \ \_____\ 
  \/_/  \/_/   \/_____/   \/_____/   \/_____/ '''

#Making an option menu to run the program
options = '''
(1)  Username Generator
(2)  Password Generator
(3)  End'''

#Our MAIN loop that 
def get_options():
  print(options)
  vo = ['1', '2', '3']
  ui = input()
  if ui not in vo:
    clear()
    print('Invalid Option')
    main()
  else:
    if ui == '1':
      clear()
      name = generate_username()
      name = name[0]
      print(name)
    if ui == '2':
      clear()
      print('How many digits in this passcode?  ')
      digits = input()
      digits = int(digits)
      full = []
      for i in range (digits):
        chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()~_+`-={}[]|\:;<>,.?/')
        char = random.choice(chars)
        full.append(char)
      full = ''.join(full)
      print(full)
    if ui == '3':
      clear()
      print(''*10000000000000000000000000000000000000)

#Main loop
def main():
  print(title)
  get_options()

#Calling our main loop
while True:
  main()
