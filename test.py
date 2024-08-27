import pyrebase

config = {"apiKey": "AIzaSyCF5Fc9dAaOz8ZltfZKK4Blqcf2J6zMR8I",
  "authDomain": "quizapp-b7016.firebaseapp.com",
  "projectId": "quizapp-b7016",
  "storageBucket": "quizapp-b7016.appspot.com",
  "messagingSenderId": "670158071667",
  "appId": "1:670158071667:web:1f7e82c3dcad1cef1d0706",
  "measurementId": "G-FPKXGP8HRS",
"databaseURL":"https://quizapp-b7016-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()

database = firebase.database()

data = {'question1':"HELLO"}

quiz=database.child("quiz").get().val()
print(len(quiz))