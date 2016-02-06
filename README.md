# WebPollApp
Django application for creating polls in a way similar to Google Forms

# Installation with Vagrant
## Install vagrant
Download and install vagrant. Add it to path if necessary. In project folder download Vagrant box and init new virtual machine. Virtualbox requires contrib added to apt debian sources

On Debian
```
sudo apt-get install vagrant virtualbox
vagrant box add ubuntu/vivid64 --provider virtualbox
vagrant up
```
Run in vagrant
```
vagrant ssh
cd /home/ilmo
python3 manage.py runserver 0.0.0.0:8000
```
Easier way is to setup IDE to handle running server. In Pycharm add remote interpreter for project, select Vagrant and change interpreter path to python3. In run settings add path mapping . = /home/ilmo and host to 0.0.0.0.

# Installation on Debian
## Packages
```
sudo apt-get install python3 python-dev python3-dev postgres python3-virtualenv libpq-dev postgresql-contrib
```


## Install python3 in virtualenv
```
virtualenv python -p python3
```

## Configure PostgreSQL
```
sudo su - postgres
createdb mydb
createuser -P username
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
```
Edit django settings respectively.

## Install python packages, setup database and create superuser
```
source python/bin/activate
pip install --upgrade -r pip_requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## Run the application
```
python manage.py runserver
```
Access the server at http://127.0.0.1:8000/admin


# TODO
* [x] Change questionnaire-question relation to many-to-many, allowing re-using popular questions
* [x] Remove answer fields from questions using only form fields
* [ ] Fix and add more validation to questions
* [x] Ordering questions
* [ ] Ordering exported answers
* [ ] More question types such as date picker
* [ ] Widget selection to question
* [ ] Fix adding new questions while creating questionnaires
* [ ] Create better UI for questionnaires
* [ ] Allow using questionnaires in iFrame
* [ ] Allow template creation and selection from admin panel
* [ ] Allow customising after-submit behaviour
* [ ] Add option to download all replies to a questionnaire(s)
* [ ] Improve downloads by renaming outputted file and sheets