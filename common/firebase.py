import pyrebase

config = {
  "apiKey": "AIzaSyBEJSw9mkG1Bn72oj5gU8c4D2aLZyuD_a0",
  "authDomain": "treatsti-fe090.firebaseapp.com",
  "databaseURL": "https://treatsti-fe090.firebaseio.com",
  "storageBucket": "treatsti-fe090.appspot.com",
  "projectId": "treatsti-fe090",
  "messagingSenderId": "499462429802"
}

firebase = pyrebase.initialize_app(config)