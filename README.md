# User managment
This is the user management web app has been developed using the Django framework and Bootstrap for the frontend. This can be integrated into any system project that needs to have a registration and login system.

### Basic Features of The App
    
* Register – Users can register and create a new profile
* Login - Registered users can login using username and password
* User Profile - Once logged in, users can create and update additional information such as address and phone number in the profile page
* Update Profile – Users can update their information such as username, email, password
* Admin Panel – admin can users with basic (username, email, password) and custom information (address, phone number)

![User Home](http://url)
![Add User](http://url)
![Add User Profile with additional fields](http://url)
![View/Update User Profile](http://url)
![User Login](http://url)
![User Registeration](http://url)

### How to run
To get this project up and running locally on your computer follow the below steps.
1. Set up a python environment
2. Run the following commands
```
$ python -m pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```   
3. Open a browser and go to http://localhost:8000/

## References
[Django Login/Logout features](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
[User management reference](https://dev.to/earthcomfy/series/14274)

