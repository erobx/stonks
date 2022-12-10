STONKS

Clone the repository and navigate into the root directory.

Run python setup.py install.
Some dependencies may or may not install, i.e. numpy, flask, and pyvis.
Install these with pip install and the respecitve name.
This project also requires sqlite3 to be installed to initalize the database.

Navigate to the stonks_app directory, ex:
C:\Users\erob7\Documents\stonks\stonks_app

Run following commands to create database file from schema.
sqlite3 stonks.db < schema.sql // OSX and Linux
sqlite3 -init schema.sql stonks.db // Powershell

On some cases you have to specify the exact path to the exe:
C:\sqlite\sqlite3.exe stonks.db < schema.sql

Run api.py from the root directory to populate the database from the csv file:
.\stonks_app\api.py

If everything worked, the database should be populated and now run wsgi.py to start the server.