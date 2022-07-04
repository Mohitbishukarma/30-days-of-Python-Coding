import firebase_admin
cred = firebase_admin.credentials.Certificate("path/totheprivatekey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL" : "url of db"
})