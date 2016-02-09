[![Build Status](https://travis-ci.org/andela-lkabui/checkpoint3.svg?branch=master)](https://travis-ci.org/andela-lkabui/checkpoint3)
[![Coverage Status](https://coveralls.io/repos/github/andela-lkabui/checkpoint3/badge.svg?branch=master)](https://coveralls.io/github/andela-lkabui/checkpoint3?branch=master)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/9f3638f3e6174272b67e4413c849d041/badge.svg)](https://www.quantifiedcode.com/app/project/9f3638f3e6174272b67e4413c849d041)

# checkpoint3

## A Django powered Bucketlist REST API

## Introduction
*  Checkpoint3 is a Django implementation of [checkpoint2](https://github.com/andela-lkabui/checkpoint2) and goes a step further to implement a frontend for the REST API using [Django Templates](https://docs.djangoproject.com/en/1.9/ref/templates/language/#templates) and [Angular JS](https://angularjs.org/)
*  Libraries and frameworks utilized include;
    *  **[Django](https://www.djangoproject.com/)** - The backbone upon which this REST API is built upon. It's a Python web framework that features models, views, url routes and user management amongst many other things
    *  **[DJ-Database-URL](https://github.com/kennethreitz/dj-database-url)** - This utility creates database connection dictionary (through its config method) from the details contained the environment variable named `DATABASE_URL`. `DATABASE_URL` is usually in the form of **`DATABASE_VENDOR://USERNAME:PASSWORD@HOST_ADDRESS:DATABASE_PORT/DATABASE_NAME`**
    *  **[Django REST framework](http://www.django-rest-framework.org/)** - This is a powerful and flexible toolkit for building APIs. It includes support for model serialization, permissions (both default and custom) and viewsets among other features.
    *  **[drf-nested-routers](https://github.com/alanjds/drf-nested-routers)** - This package provides routers that allow for the creation of nested resources from Django Rest Framework viewsets.
    *  **[Django REST Swagger](https://github.com/marcgibbons/django-rest-swagger)** - This package is built on top of `Django REST Framework`. It generates documentation content based on the `docstring documentation`, `class titles`, `method arguments` etc from `Django REST Framework` viewsets,
    *  **[fake-factory](https://pypi.python.org/pypi/fake-factory)** - This API employs the use of this library in the unittests. It generates random values for input when testing.
    *  **[ipdb](https://pypi.python.org/pypi/ipdb)** - The Python debugger. Very useful during development.

## Installation and Setup
*  Navigate to a directory of choice on terminal
*  Clone this repository on that directory.
  *  Using ssh;
    *  `git@github.com:andela-lkabui/checkpoint3.git`
  *  Using http;
    *  `https://github.com/andela-lkabui/checkpoint3.git`
* Navigate to the repo's folder
    *  `cd checkpoint3/`
*  Install the project's backend dependencies
  *  `pip install -r requirements`
*  Install the project's database. PostgreSQL was used for this task. Please locate your platform and follow the installation instructions [here](http://www.postgresql.org/download/)
*  Install the project's front end dependencies using [bower](http://bower.io/).
  *  `bower install <citation needed>`


 ```Please note that in order to use bower, you need to have node, npm and git installed on your system```

*  After installation of the dependencies above, create a database on PostgreSQL for this app.
*  Set the environment variable **`DATABASE_URL`** with the **username**, **password**, **port** and **database name**. Refer to the structure of **`DATABASE_URL`** in the introduction section above.
*  Create and apply migrations
  *  `python manage makemigrations api`
  *  `python manage migrate api`
*  Run the app
  *  `python manage runserver`

## Routes, methods and functionality
*  To view this API's documentation, visit `/api/docs` while the app is running and explore the resources and associated actions it has to offer.

## Tests
*  The tests have been written in Python's `unittest` module.
*  The tests are run with the coverage package to facilitate the creation of test coverage reports.
*  To run the tests, first ensure you are in the project's root folder (where the file requirements.txt is located)
*  Issue the following command on terminal.
  *  `coverage run -m unittest discover tests`
*  The tests are successful if they run without failures or errors
  ```
  .............................
  ----------------------------------------------------------------------
  Ran 29 tests in 27.776s

  OK
  ```
*  To view test coverage, run the following command.
  *  `coverage report -m`
