# webdevassignment
Created Webapplication using Django with MongoDB Connect(local database)
Setting up MongoDB Database for Django Application:
Step-1: Download MongoDB from https://www.mongodb.com/try/download/community 
Step-2: Add path to the environmental variables
Step-3: Open MongoDB Connect and click on Connect. It will get connected to localhost:27017
Step-4: Click on Create Database. Enter Details of DataBase Name and Collection Name

Procedure to Create Django Project:
Step-1: Open Terminal(or)Command Prompt
Step-2: Type pip install django
Step-3: Create a django project using command "django-admin startproject projectname"
Step-4: pip install djongo
Step-5: Changing settings.py file to connect to MongoDB Database.Change the DATABASES in settings.py
DATABASES={
  'default':{
'ENGINE': 'djongo',
'NAME': 'your-db-name',
'CLIENT': {
  'host':'localhost',
  'port': 27017,
  'username': '',
  'password': ''
}
 }
}
Step-6: Run python manage.py makemigrations
Step-7: Run python manage.py migrate (to enable the changes)
Step-8: Run python manage.py startapp appname --Creating the apps
Add the created app in Installed_Apps in settings.py file
Step-9: Create required html files in template folder. Add urls and views.

