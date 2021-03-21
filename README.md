# Shopping-cart
A shopping cart project created using Flask, postgreSQL, SQLAlchemy, HTML, CSS, and JavaScript.

# To run locally:
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

3. Run the following exports: 
```sh
    $ APP_SETTINGS="config.DevelopmentConfig"
    $ FLASK_APP=flaskr
    $ FLASK_ENV=development
```

4. Create the database by running the following shell script:
```sh
    $ sh bin/create-db.sh
```

5. To create the tables, while inside virtual environment:
```sh
    $ cd flaskr
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
```
