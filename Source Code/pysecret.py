#flag=imp
#[ stable release ] 

# Pysecret
# Copyright (C) 2018-2019 M.Anish <aneesh25861@gmail.com>
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

''' Pysecret is a simple secret sharing tool using python3 developed by M.Anish only.
    Converts secrets to more than one code . The secret can't be recovered even if a single code is missing'''
try:
    import os
    import getpass
    import secrets
except ImportError:
    print('Critical Error: Required Modules Not found!\n')
    x=input('Press any key to continue...')
    exit(1)

A=((0,'A'),(1,'B'),(2,'C'),(3,'D'),(4,'E'),(5,'F'),(6,'G'),(7,'H'),(8,'I'),(9,'J'),(10,'K'),(11,'L'),(12,'M'),(13,'N'),(14,'o'),(15,'P'),(16,'Q'),(17,'R'),(18,'S'),(19,'T'),(20,'U'),(21,'V'),(22,'W'),(23,'X'),(24,'Y'),(25,'Z'),(26,'0'),(27,'1'),(28,'2'),(29,'3'),(30,'4'),(31,'5'),(32,'6'),(33,'7'),(34,'8'),(35,'9'))
A=list(A)
secrets.SystemRandom().shuffle(A)
A=tuple(A)

#converts Alphanumeric characters to numbers of base 36    
def f(x):
  store=[]
  for s in x:
    count=0
    for i in range(36):
        if A[i][1].lower()==s.lower():
          store.append(A[i][0])
          count=1
          break
    if count==0:
      store.append(' ')
  return tuple(store)                
    
#converts base 36 numbers to alphanumeric charactors.
def rf(x):
  store=[]
  q=''
  for s in x:
    count=0
    for i in range(36):
        if A[i][0]==s:
          store.append(A[i][1])
          count=1
          break
    if count==0:
      store.append(' ')
  q=''.join(store)
  return q
    

#generates a key without keyfile.
def ikey(x):
    seed=list(range(36))
    masterkey=[]
    for i in range(len(x)):
        masterkey.append(secrets.choice(seed))
    m=tuple(masterkey)
    return m

#encrypts a given string and returns ciphertxt and key as a tuple. (no file generated!)
def en(msg):
    ciphertxt=[]
    x=f(msg)
    y=ikey(msg)
    if len(x)<=len(y):
        for i in range(len(x)):
            if type(x[i])==int and type(y[i])==int:
                ciphertxt.append(((x[i]+y[i])%36))
            else:
                ciphertxt.append(' ')
    else:
        x=input('Press any key to continue...')
        exit(1)
    ciphertxt=tuple(ciphertxt)
    ctxt=rf(ciphertxt)
    shk=rf(y)
    return (ctxt,shk)

#decrypts a given encrypted string and returns a plaintxt as output.
def de(c,k):
    ciphertxt=[]
    x=f(c)
    y=f(k)
    if len(x)<=len(y):
        for i in range(len(x)):
            if type(x[i])==int and type(y[i])==int:
                ciphertxt.append(((x[i]-y[i])%36))
            else:
                ciphertxt.append(' ')
    else:
        x=input('Press any key to continue...')
        exit(1)
    ciphertxt=tuple(ciphertxt)
    ctxt=rf(ciphertxt)
    return (ctxt)

#function for secret splitting interface.
def sprocess():
    table=[]
    print('''\n         ---------------------------------------------------------
               |            Secret splitting                   |
         -----------------------------------------------------------''')
    while(1):
        try:
            x=int(input('\nEnter the number of shares(atmost 10,atleast 2):'))
            if(x<11)and(x>1):
                break
        except ValueError:
            print('\nPlease enter a valid integer greater than 1 but less than or equal to 10!\n')
    msg=getpass.getpass('Enter the secret:')
    table+=list(en(msg))
    for i in range(2,x):
        tmp=table[-1]
        table.pop()
        table+=list(en(tmp))
    for i in range(len(table)):
        print('SHARE',i+1,':',table[i])

#function for secret combining interface.
def cprocess():
    table=[]
    print('''\n          ---------------------------------------------------------
                |          Secret Combine                     |
          -----------------------------------------------------------''')
    while(1):
        try:
            x=int(input('\nEnter no. of shares to combine(atmost 10,atleast 2):'))
            if(x<11)and(x>1):
                break
        except ValueError:
                print('\nPlease enter a valid integer greater than 1 but less than or equal to 10!\n')
    for i in range(x):
            table.append(getpass.getpass(str('Enter Share '+str(i+1)+':')))
    for i in range(x-1):
            hook=[]
            a,b=table[-2],table[-1]
            table.pop()
            table.pop()
            hook.append(de(a,b))
            table+=hook
    print()
    print(''.join(table))
        

def start():
    print('\n<-----Task Started----->\n')
    
def end():
    print('\n<-----Task Completed----->\n')

def tsks():
    start()
    
def tske():
    end()

def tskf():
    print('\n<-----Task Failed !----->\n')


def wait():
      x=input('\nPress any key to continue...\n')

def display(file):
        if os.path.exists(file)==False:
           print('Error: '+file+' not found!')
           wait()
           exit(1)
        with open(file,'r') as f:
            s=f.read(1024)
            print(s)
            while len(s)>0:
                s=f.read(1024)
                print(s)

# function for main interface.    
def mm():
   print('''\n           ---------------------------------------------------------------
               |   PYSECRET: SIMPLE SECRET SHARING USING PYTHON       |
           ---------------------------------------------------------------''')
   print('\n1)Split a secret into codes.')
   print('2)Combine codes to recover secret.')
   cmd=input('\nEnter command:')
   if cmd=='1':
       sprocess()
       mm()
   elif cmd=='2':
       cprocess()
       mm()
   elif cmd.lower()=='c' or cmd.lower()=='close':
      exit()
   else:
      print('please enter 1 or 2 or \'c to exit!')
      mm()
   exit()


mm()
    
   
        
        
