# User managment
This is the user management web app has been developed using the Python Django framework. This can be integrated into any system project that needs to have a registration and login system.

### Features     
* User home - Landing page for users/visitors
![User Home](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_home.jpg)

* Sign up – Users can register and create a new profile
![User Sign up](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_user_sign_up.jpg)

* View/Update Profile - Once logged in, users can create and update the basic user profile information (address details, phone number)
![Admin Panel for add/update user profile with custom fields](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_view_profile.jpg)

* Sign in - Registered users can login using username and password
![User Sign in](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_user_sign_in.jpg)

* Admin Panel for adding/updating users – admin can add/update users with basic user information (username, email, password, first name, last name) and custom profile information (address details, phone number, location)
![User profile view](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_view_profile.jpg)

* Users location view : A single map page to view all users locations
![Map with all user locations](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_map_with_all_user_locations.jpg)

* Admin Panel for viewing user audit log – admin can view the user activities like login, logout, and requests.
![Activity user activity audit log](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_audit_log.jpg)

* Admin Panel for viewing profile audit log – admin can view the profile field updates (user profile model updates)
![Activity user profile attribute change audit log](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_profile_attribute_audit_log.jpg)

### How to run
To get this project up and running locally on your computer follow the below steps.
1. Set up a python environment
2. Run the following commands
```
$ python -m pip install -r requirements.txt
$ python manage.py migrate
``` 
3. Execute unit tests
```
$ python manage.py test
```
4. Create admin user
```
$ python manage.py createsuperuser
```
4. Start the server
```
$ python manage.py runserver
```
5. Open a browser and go to http://localhost:8000/

## References
[Django Login/Logout features](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
[User management reference](https://dev.to/earthcomfy/series/14274)

