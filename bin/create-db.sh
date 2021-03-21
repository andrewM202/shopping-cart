#!/bin/sh

# Create Application Database and User

# This script will use the 'psql' command to run SQL commands
# that will create the needed database and user for this application
# A running postgreSQL server is necessary
#
# NOTE: You only need to run this script once.
# NOTE: Inspiration for this create-db document from Zach Fedor.
# 
# Run with the following command in the project's root directory:
# $ sh bin/create-db.sh

# create user for the application
psql postgres -c 'CREATE USER shopcart_user;'

# create development database and grant access to application user
psql postgres -c 'CREATE DATABASE shopping_cart;'
psql postgres -c 'GRANT ALL PRIVILEGES ON DATABASE "shopping_cart" to shopcart_user;'
psql postgres -c 'GRANT SELECT ON ALL TABLES IN schema public TO shopcart_user;'
psql postgres -c 'GRANT CONNECT ON DATABASE shopping_cart TO shopcart_user;'
psql postgres -c 'GRANT DELETE ON ALL TABLES IN schema public TO shopcart_user;'

