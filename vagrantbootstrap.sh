#!/usr/bin/env bash
set -e
cd /home/ilmo
sudo apt-get update
sudo apt-get install -y python3 python-dev python3-dev postgresql libpq-dev postgresql-contrib python3-pip

sudo su - postgres -c "
createdb pollwebapp
psql -c \"CREATE USER pollwebappuser WITH PASSWORD 'moomoo';\"
psql -c \"GRANT ALL PRIVILEGES ON DATABASE pollwebapp TO pollwebappuser\";
"
sudo pip3 install --upgrade -r pip_requirements.txt

python3 manage.py migrate
python3 -c "
import os
os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"ilmo.settings\")
import django
django.setup()
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'password').save()
"
