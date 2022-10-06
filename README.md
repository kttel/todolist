# To do list [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

To do list is a Python Django application that 

## Features

- you can register your account using custom login and password;
- you can login into your account using your login and password;
- you can add various tasks with its title, description and status;
- you can delete your created tasks.

## Steps to be followed for first time use
- run this command to clone this repository
```bash
git clone https://github.com/kttel/todolist.git
```
- in project run this commands to work with database
```bash
python manage.py makemigrations

python manage.py migrate
```
- create superuser to work with admin panel 
```
python manage.py createsuperuser
```
## Usage

- in the directory with manage.py file run rhis command
```
python manage.py runserver
```

## Contributing
Various pull requests are welcome. Project can be updated in any time.

Last update: 06.10.2022
