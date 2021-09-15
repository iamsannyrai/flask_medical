# Medical Application

### Project Setup for development
1. Navigate inside project folder.
2. Activate virtual environment by typing `source venv/bin/activate` in your terminal.
3. Type `pip install requirements.txt` to install all the requirements packages required to run the project.
4. Finally, type `flask run wsgi_dev.py` to run the app in development or debug mode. 


### Flask Migrate official documentation
[Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

### To run migrations for development
Type following in terminal:

> export FLASK_APP=wsgi_dev
> 
> export FLASK_ENV=development
> 
> flask db migrate -m  "your_message".
> 
> flask db upgrade







