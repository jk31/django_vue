# Django + Vue Template for Heroku

## Features

* Backend
  * Django 3
  * Ready for deployment on Heroku
  * REST API
    * API keys (TODO)
  * Backend User management
    * Custom user model
      * https://testdriven.io/blog/django-custom-user-model/
      * https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
      * https://learndjango.com/tutorials/django-best-practices-referencing-user-model
    * Full user authentication and authorization workflow (registration, login, email activation, password reset etc.)
    * Cookie sessions / Token sessions (TODO)
  * S3 Bucket storage for files (TODO)
  * Subscription to services (TODO)
    * Stripe integration
* Frontend
  * Vue 2

## Clone and recreate git instance.

```bash
git clone ...

rm -rf .git

git init

git add .

git commit -m 'init'

git branch -M main
```

## Deployment

### Required buildpacks (under Heroku settings)

* `heroku/python`
* `heroku/nodejs`

### Required enviromental variables (so far)

* `DISABLE_COLLECTSTATIC = 1`
* `SECRET_KEY`
* `EMAIL_HOST`
* `EMAIL_USERNAME`
* `EMAIL_PASSWORD`

### Before Deployment

Read [official Django deployment checklist](https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/).

`settings.py`:
- [ ] Turn of Debugging
- [ ] Change Email Backend in 
- [ ] Secure cookies
- [ ] Secure `SECRET_KEY` 
- [ ] Setup environmental variables on the deployment server
- [ ] Have correct migrations files for the database

- [ ] Change `runtime.txt` python version


### [Heroku CLI Deployment](https://devcenter.heroku.com/articles/getting-started-with-python)

* [Heroku CLI cheatsheet](https://devhints.io/heroku)

```bash
# Login to heroku via CLI
heroku login

# Create empty app on heroku
heroku create --region eu

# Deploy code to heroku
git push heroku main

# Open heroku bash for following commands
heroku run bash

# Migrate database based on migration files
python manage.py migrate

# Creat admin account
python manage.py createsuperuser
```

If you want to build on the heroku instance:
```
# Clean node packages and install dependacies to be able to build the frontend
rm -rf node_modules package-lock.json && npm install && npm install --only=dev

# Build frontend files
npm run build

# Collect static files from the frontend build for Django
python manage.py collectstatic
```

Useful heroku commands:

```bash
# List all apps
heroku apps

# Delete app
heroku apps:destroy --app APPNAME

# Logs
heroku logs
heroku logs -t

# Deploy a branch
git push heroku branch_name:master
```

## Backend Development

### Requirements so far

* [Django](https://www.djangoproject.com/)
* [Django Heroku](https://devcenter.heroku.com/articles/django-app-configuration)
* [Django REST Framework](https://www.google.com)
* [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
* [Django CORS Headers](https://pypi.org/project/django-cors-headers/)


### Development

```bash
# Install requiremed packages
pip install -r requirements.txt

# Update for migrations and create local database
python manage.py makemigrations users
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```


## Frontend Development

```
npm install
npm run serve
```
