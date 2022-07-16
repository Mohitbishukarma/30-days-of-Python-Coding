# connecting to firebase admin sdk
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("storemanagement-private-key.json")
firebase_admin.initialize_app(cred,{
    "databaseURL" : "..."
})


# pushing data to db using set() function
from firebase_admin import db
import json

# ref = db.reference("/")
# with open("user.json") as f:
#     data = json.load(f)
# ref.set(data)

# getting data from firebase db 
ref = db.reference("/")
username = input("Enter Your Username : ")
password =  input("Enter Your Password : ")

data = ref.get()
for key,value in data.items():
    # print( f"{key} : {value}")
    # print(value["name"]==username.strip() and value["password"] == password.strip() )
    if value["name"]==username.strip() and value["password"] == password.strip() :
        print(f"Hello {value['name']} \nWelcome to connectStudent.com")
   
