Django Welcome App

This is a simple Django project that displays a custom welcome message on the homepage:

“Hello, world. You're at the myapp index.”

The project was created as part of a challenge to practice creating Django projects, apps, URL mappings, view functions, and templates.

🚀 Features

Homepage with a custom welcome message

Organized Django app structure

Easy setup with virtual environment support

📂 Project Structure
myproject/
│── manage.py
│── myproject/        # Main project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│── myapp/            # Custom Django app
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── home.html
│   └── migrations/
│
└── README.md

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/eddyfranc/eddyfranc.git
cd djangostarter

2. Create and activate a virtual environment
python -m venv virtualenv
# On Mac/Linux
source virtualenv/bin/activate
# On Windows
virtualenv\Scripts\activate

3. Install dependencies
pip install django

4. Run migrations
python manage.py migrate

5. Run the development server
python manage.py runserver

6. Open the app

Go to your browser and visit:
👉 http://127.0.0.1:8000/

You should see:
“Hello, world. You're at the myapp index”

🖇️ URL Mapping

Project urls.py (myproject/urls.py):

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Root route points to myapp
]


App urls.py (myapp/urls.py):

from django.urls import path
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
]

👀 Views and Template

View Function (myapp/views.py):

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


Template (myapp/templates/index.html):

<!DOCTYPE html>
<html>
<head>
    <title>My Django App</title>
</head>
<body>
    <h1>Hello, world. You're at the myapp index.</h1>
</body>
</html>
