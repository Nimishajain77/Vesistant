import pyrebase

#conifiguration credentials to connect you to firebase
firebaseConfig = {
  'apiKey': "AIzaSyBZ2RRLtGzD96ITIdrO7MMLw393eeqiueM",
  'authDomain': "firestore-ff42f.firebaseapp.com",
  'projectId': "firestore-ff42f",
  'storageBucket': "firestore-ff42f.appspot.com",
  'messagingSenderId': "992174412197",
  'appId': "1:992174412197:web:b8993a965bb36f27efd84c",
  'measurementId': "G-9E3Z720L8R",
  'databaseURL':"https://console.firebase.google.com/u/0/project/firestore-ff42f/overview"
}

#initialize an app with the above provided configuration details
firebase=pyrebase.initialize_app(firebaseConfig)

#db=firebase.database()
#auth=firebase.auth()
storage=firebase.storage()

#Authentication
#Registration
#email=input("\nEnter your Email\n")
#password=input("\nEnter your password\n")
#confirmpass=input("\nConfirm password\n")
#if password==confirmpass:
#    try:
#        auth.create_user_with_email_and_password(email,password)
#        print("\nSuccess!\n")
#    except:
#        print("\nUsername already exists\n")
#else:
#    pass

#Login
#try:
#    email=input("\nEnter your email\n")
#    password=input("\nEnter your password\n")
#    auth.sign_in_with_email_and_password(email,password)
#    print("\nLogin Successful\n")
#except:
#    print("Invalid email or password..Please try again!!")

#Storage
filename=input("Enter the name of the file you want to upload")
cloudfilename=input ("Enter the name of the file on the cloud")
storage.child(cloudfilename).put(filename)