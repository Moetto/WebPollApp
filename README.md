# WebPollApp
Django application for creating polls in a way similar to Google Forms

# Installation on debian
## Packages
'''
sudo apt-get install python3 python-dev python3-dev postgres python3-virtualenv libpq-dev postgresql-contrib
'''

## Install python3 in virtualenv
'''
virtualenv python -p python3
'''

## Configure PostgreSQL
'''
sudo su - postgres
createdb mydb
createuser -P username
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
'''
Edit django settings respectively.

## Install python packages, setup database and create superuser
'''
source python/bin/activate
pip install --upgrade -r pip_requirements.txt
python manage.py migrate
python manage.py createsuperuser
'''

## Run the application
'''
python manage.py runserver
'''
Access the server at http://127.0.0.1/admin


# TODO
* Change questionnaire-question relation to many-to-many, allowing re-using popular questions
* Remove answer fields from questions using only form fields
* Fix and add more validation to questions
* Ordering questions
* Ordering exported answers
* More question types such as date picker
* Widget selection to question
