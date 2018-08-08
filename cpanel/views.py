from django.shortcuts import render
import pyrebase


# Initialize Firebase
config = {
"apiKey": "AIzaSyDYxrIRcJBwuGYmcM_OuMDuqqHgEpKYxd0",
"authDomain": "asaleem-firebase.firebaseapp.com",
"databaseURL": "https://asaleem-firebase.firebaseio.com",
"projectId": "asaleem-firebase",
"storageBucket": "asaleem-firebase.appspot.com",
"messagingSenderId": "415533361545"
};

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signin(request):
    return render (request, "signin.html")

def postsignin(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')

    try:
        user= auth.sign_in_with_email_and_password(email, password)
    except:
        message = "invalid credentials"
        return render(request, "signin.html", {"message":message})
    print (user)
    return render (request, "welcome.html", {"e":email})