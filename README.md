# Shopping-cart
This application has been deployed live at https://shopping-cart952.herokuapp.com/

A shopping cart application created using Flask, postgreSQL, SQLAlchemy, HTML, CSS, and JavaScript. Items can be viewed, added, or deleted from the cart. A page to finalize shopping transactions (currently just uses DOM to change text, no other functionality) is included. 

# To Run The Application Locally:
NOTE: postgres must be downloaded 
```sh
    $ brew install postgres 
    $ brew services start postgres
```

1. Create and activate the virtual environment
```sh
    $ python3 -m venv venv
    $ source venv/bin/activate
```

2. Install the dependencies 
```sh
    $ python3 -r requirements.txt
```

3. Run the following exports 
```sh
    $ FLASK_APP=flaskr
    $ FLASK_ENV=development
    $ export APP_SETTINGS="config.DevelopmentConfig"
    $ export DATABASE_URL="postgresql:///shopping_cart"
```

4. Create the database by running the following shell script
```sh
    $ sh bin/create-db.sh
```

5. Create the tables while inside the virtual environment
```sh
    $ cd flaskr
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
```

6. Run the application while inside the flaskr directory. Then open the live application at http://127.0.0.1:5000/
```sh
   $ flask run 
```

# Screenshots of Website Below
<img width="1208" alt="sceen1" src="https://user-images.githubusercontent.com/70407217/111922897-ee121780-8a72-11eb-8ca8-6a038be385e4.png">
<img width="1203" alt="screen2" src="https://user-images.githubusercontent.com/70407217/111922906-fc603380-8a72-11eb-9ef8-e7607c9636c7.png">
<img width="1208" alt="screen3" src="https://user-images.githubusercontent.com/70407217/111922911-0124e780-8a73-11eb-87b9-70bcf2c8c4bd.png">

