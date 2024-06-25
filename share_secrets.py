
# share_secret
# Copyright (C) 2018-2023 M.Anish <aneesh25861@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

''' 

Share_secret is a simple secret sharing tool using python3 
developed by M.Anish only.
Converts secrets to more than one code . The secret can't be 
recovered even if a single code is missing

'''
try:
    import getpass
    import secrets
    import sys
    from typing import Union
except ImportError:
    print('Critical Error: Required Modules Not found!\n')
    null: str = input('Press any key to continue...')
    sys.exit(1)

ALPHABET: tuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


# converts Alphanumeric characters to numbers of base 36    
def alpha_to_base36(alpha_str: Union[str, tuple]) -> tuple:
  store: list = []
  for char in alpha_str:
    count: int = 0
    for i in range(36):
        if ALPHABET[i].lower() == char.lower():
          store.append(i)
          count = 1
          break
    if count == 0:
      store.append(' ')
  return tuple(store)                

    
# converts base 36 numbers to alphanumeric charactors.
def base36_to_alpha(base36: tuple) -> str:
    store: list[str] = []
    alpha: str = ''
    for char in base36:
        try:
            store.append(ALPHABET[char])
        except(IndexError, TypeError):
            store.append(' ')
    alpha = ''.join(store)
    return alpha
    

# generates a key without keyfile.
def ikey(message: str) -> tuple:
    seed: list = list(range(36))
    masterkey: list = []
    for i in range(len(message)):
        masterkey.append(secrets.choice(seed))
    return tuple(masterkey)


# encrypts a given string and returns ciphertxt and key as a tuple. (no file generated!)
def encrypt(message: str) -> tuple:
    ciphertxt: list[str] = []
    x: tuple = alpha_to_base36(message)
    y: tuple = ikey(message)
    for i in range(len(x)):
            if isinstance(x[i], int):
                ciphertxt.append(((x[i]+y[i]) % 36))
            else:
                ciphertxt.append(' ')
    ctxt: str = base36_to_alpha(tuple(ciphertxt))
    shk: str = base36_to_alpha(y)
    return (ctxt, shk)


# decrypts a given encrypted string and returns a plaintxt as output.
def decrypt(c: str, k:str) -> str:
    ciphertxt: list = []
    x: tuple = alpha_to_base36(c)
    y: tuple = alpha_to_base36(k)
    if len(x) <= len(y):
        for i in range(len(x)):
            if isinstance(x[i], int) and isinstance(y[i], int):
                ciphertxt.append(((x[i]-y[i]) % 36))
            else:
                ciphertxt.append(' ')
    else:
        input('Incorrect Input!!!\nPress any key to continue...')
        sys.exit(1)
    return base36_to_alpha(tuple(ciphertxt))

    
# function for secret splitting interface.
def sprocess():
    table: list = []
    print('''\n         ---------------------------------------------------------
               |            Secret splitting                   |
         -----------------------------------------------------------''')
    while 1:
        try:
            x = int(input('\nEnter the number of shares(atmost 10,atleast 2): '))
            if 1 < x < 11:
                break
        except ValueError:
            print('\nPlease enter a valid integer greater than 1 but less than or equal to 10!\n')
    msg: str = getpass.getpass('Enter the secret: ')
    table += list(encrypt(msg))
    for i in range(2, x):
        tmp: str = table[-1]
        table.pop()
        table += list(encrypt(tmp))
    for i in range(len(table)):
        print('SHARE', i+1, ':', table[i])


# function for secret combining interface.
def cprocess() -> None:
    table: list = []
    print('''\n          ---------------------------------------------------------
                |          Secret Combine                     |
          -----------------------------------------------------------''')
    while 1:
        try:
            x: int = int(input('\nEnter no. of shares to combine(atmost 10,atleast 2): '))
            if 1 < x < 11:
                break
        except ValueError:
                print('\nPlease enter a valid integer greater than 1 but less than or equal to 10!\n')
    for i in range(x):
            table.append(getpass.getpass(str('Enter Share '+str(i+1)+': ')))
    for i in range(x-1):
            hook: list = []
            a, b = table[-2], table[-1]
            table.pop()
            table.pop()
            hook.append(decrypt(a, b))
            table += hook
    print()
    print(''.join(table))
        

# function for main interface.    
def mm() -> None:
   print('''\n           ---------------------------------------------------------------------
               |   SHARE-SECRET: SIMPLE SECRET SHARING USING PYTHON       |
           ---------------------------------------------------------------------''')
   print('\n1) Split a secret into codes.')
   print('2) Combine codes to recover secret.')
   print('3) Quit application.')
   cmd: str = input('\nEnter choice: ')
   if cmd == '1':
       sprocess()
   elif cmd == '2':
       cprocess()
   elif cmd == '3':
       sys.exit(0)
   else:
      print('\nplease enter 1, 2 or 3 to select options or press ctrl + c to exit!')
      

while True:
    try:
        mm()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)
