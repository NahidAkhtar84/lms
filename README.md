# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

## Getting Started:
The project, Lunch Management System, can be run locally creating a python environment file and also can be run on Docker. Lets see how we will run the project with a virtual environemnt and with docker.

### Through creating virtual environment
***
process has been described for linux
***

1. Go to root directory of the project and enter to the project directory with the command
```
cd lunch_management_system
```
2. Install the package
```
apt-get install python3-venv 
```
3. Create virtual environment directory
```
mkdir djangoenv
```
4. Create virtual environment
```
python3 -m venv djangoenv
```
5. Activate virtual environment
```
source djangoenv/bin/activate
```
6. Install the required packages from requirements.txt file. For thi, after activation of virtual environment run following command-
```
pip install -r requirements.txt
```
>>> note that, you must install python environment and pip before

7. Now run the project-
```
python manage.py runserver
```
8. For creating migrations-
```
python manage.py makemigrations
```
and then,
```
python manage.py migrate
```

9. For creating super user-
```
python manage.py createsuperuser
```
You can see the project admin panel at-
http://localhost:8000/admin/

You will see swagger api documentation at-
http://localhost:8000/api/docs/

### Through docker
To run project with docker, Firstly you have to build the project-
```
docker-compose build
```
It will take some times to install all the docker images and to configure the project
Then to run the project you have to write following command-
```
docker-compose up
```
You can build and run the project at the same time-
```
docker-compose up --build
```
To run particular django commands, use-
```
docker-compose run web ---(django command)---
```
For example:
```
docker-compose run web python manage.py shell
```
```
docker-compose run web python manage.py runserver
```
etc

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact