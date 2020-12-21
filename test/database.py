import pyrebase


firebaseConfig={
    "apiKey": "AIzaSyBYVwVZUBLXSm7iR5Fp6k-dziJGEuhwExk",
    "authDomain": "megaboth007.firebaseapp.com",
    "databaseURL": "https://megaboth007.firebaseio.com",
    "projectId": "megaboth007",
    "storageBucket": "megaboth007.appspot.com",
    "messagingSenderId": "942424390212",
    "appId": "1:942424390212:web:c3622743b0fba57b5a1a11"
    }
firebase = pyrebase.initialize_app(firebaseConfig)

db=firebase.database()