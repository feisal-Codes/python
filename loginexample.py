import json

filename="/home/fesal/Desktop/pythonpractise /thinkPython/details.json"

count=3

def details():
    details=dict()
    
    while True:
     name=input('Set A username:or press 1 to quit \n')
     deta=load_details()

     if name=='1':
         break
     if check_if_user_exist(name,deta)==True:
         sign_in(deta,name)
         break
     if check_if_user_exist(name,deta)==False:
        new_user(details,deta,name)
        break     
     
    return details
def store_details(details):
    with open(filename, 'w') as outfile:
      json.dump(details, outfile)
    
def load_details():
    with open(filename) as json_file:
      details = json.load(json_file)
    return details


def check_if_user_exist(name,deta):
      
    if name  in deta.keys(): 
         print( name+' you are already registered' )
         
         return True
    
    return False
    
def new_user(details,deta,name):
   
    print(name.title() + ' You are not in our database ')
    while True:
     name2=input('enter your name to register:')
     if name2=='1':
         break

     pasword=input('set a password: ')
     details=deta
     details.update({name2:pasword})
     print('registration successful')
     print('register another user:or press 1 to Quit  ')
     store_details(details)



def sign_in(details,name):
    global count
    while count > 0:
     count-=1

     password=input('please enter your password: ')
     if details[name]==password:
        print('sign in successful')
        return
     elif details[name] != password:
         print('wrong password,you have: '+str(count) +' attempts remaining')
       
       
        
details()