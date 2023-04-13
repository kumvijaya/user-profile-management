# User profile management
This is the user profile management web app built using the Python Django framework. This can be integrated into any system/application project that needs to have a registration and login system.

### Features     
* #### User home: Landing page for users/visitors
![User Home](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_home.jpg)

* #### Sign up: Users can register and create a new profile
![User Sign up](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_user_sign_up.jpg)

* #### View/Update Profile - Once logged in, users can create and update the basic user profile information (address details, phone number)
![User profile view](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_view_profile.jpg)

* #### Sign in: Registered users can login using username and password
![User Sign in](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_user_sign_in.jpg)

* #### Admin Panel for adding/updating users: Admin can add/update users with basic user information (username, email, password, first name, last name) and custom profile information (address details, phone number, location)
![Admin Panel for add/update user profile with custom fields](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_add_custom_profile.jpg)

* #### Users location view : A single map page to view all users locations
![Map with all user locations](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_map_with_all_user_locations.jpg)

* #### Admin Panel for viewing user audit log: Admin can view the user activities like login, logout, and requests.
![Activity user activity audit log](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_audit_log.jpg)

* #### Admin Panel for viewing profile audit log: Admin can view the profile field updates (user profile model updates)
![Activity user profile attribute change audit log](https://github.com/kumvijaya/user_management/blob/main/images/screenshot_profile_attribute_audit_log.jpg)

### How to run
To get this project up and running locally on your computer follow the below steps.
1. Set up a python environment
2. Add .env file in project root with
```
SECRET_KEY=<<App secret key>>
GOOGLE_API_KEY=<<App secret key>>
```
* App secret key: Can be generated with django shell using [get_random_secret_key()](https://codinggear.blog/django-generate-secret-key/)
* Google API key: Use your valid google api key for map access
3. Install dependencies
```
$ python -m pip install -r requirements.txt
```
3. Setup database
```
$ python manage.py migrate
``` 
4. Execute unit tests
```
$ python manage.py test
```
5. Create admin user
```
$ python manage.py createsuperuser
```
6. Start the server
```
$ python manage.py runserver
```
7. Open a browser and go to http://localhost:8000/

## References
* [Django Login/Logout features](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
* [User management reference](https://dev.to/earthcomfy/series/14274)

