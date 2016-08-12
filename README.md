# Guidance website
This is a website to manage the presence for the helping session (guidance) of the Brussels Polytechnic School 
### Requirement
The only requirement is to have a python version and git installed
### Local deployment
1. Clone the repository
    ```
    git clone https://github.com/bakboka/presences.git
    ```
2. Create a virtual environment. If you do not have virtualenv install do it with the command below
    ```
    pip install virtualenv
    ```
    then run the following to create a virtual environment in your current directory
    ```
    virtualenv venv
    ```
    finally active this virtual environment with 
    ```
    source venv/bin/activate
    ```
3. Install the requirements with the following command
    ```
    pip install -r requirement.txt
    ```
4. Create a file called secret_key.txt in the folder guidance and put your secret key in it. This key can be generated with this [website](http://www.miniwebtool.com/django-secret-key-generator/)

5. Create a file called database.json and put you database configuration in it. The file must contain a valid json. The configuration is defined [here](https://docs.djangoproject.com/en/1.10/ref/settings/#databases)
6. Migrate the django app with the following command. Nb: you need to be in the root directory of the repository.
    ```
    ./manage.py migrate
    ```
7. Load the fixture 
    ```
    ./manage.py loaddata fixture/db.json
    ```
8. Finally run the server 
    ```
    ./manage.py runserver
    ```


