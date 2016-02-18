[![Build Status](https://travis-ci.org/andela-lkabui/checkpoint3.svg?branch=develop)](https://travis-ci.org/andela-lkabui/checkpoint3)
[![Coverage Status](https://coveralls.io/repos/github/andela-lkabui/checkpoint3/badge.svg?branch=develop)](https://coveralls.io/github/andela-lkabui/checkpoint3?branch=develop)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/9f3638f3e6174272b67e4413c849d041/badge.svg)](https://www.quantifiedcode.com/app/project/9f3638f3e6174272b67e4413c849d041)

# checkpoint3

## A Django powered Bucketlist REST API

## Introduction
*  Checkpoint3 is a Django implementation of [checkpoint2](https://github.com/andela-lkabui/checkpoint2) and goes a step further to implement a frontend for the REST API using [Django Templates](https://docs.djangoproject.com/en/1.9/ref/templates/language/#templates) and [Angular JS](https://angularjs.org/)

## Dependencies

### Back End Dependencies
*  Several python packages were used to wire up the functionality of the backend. These include;
    *  **[Django](https://www.djangoproject.com/)** - The backbone upon which this REST API is built upon. It's a Python web framework that features models, views, url routes and user management among many other features.
    *  **[DJ-Database-URL](https://github.com/kennethreitz/dj-database-url)** - This utility creates a database connection dictionary (through its config method) from the details contained the environment variable named **`DATABASE_URL`**.
      *  **`DATABASE_URL`** is usually in the form of:
        *  **`DATABASE_VENDOR`**://**`DATABASE_USERNAME`**:**`DATABASE_PASSWORD`**@**`HOST_ADDRESS`**:**`DATABASE_PORT`**/**`DATABASE_NAME`**
    *  **[Django REST framework](http://www.django-rest-framework.org/)** - This is a powerful and flexible toolkit for building browsable REST APIs. It includes support for model serialization, permissions (default and custom) and viewsets among other features.
    *  **[drf-nested-routers](https://github.com/alanjds/drf-nested-routers)** - This package provides routers that allow for the creation of nested resources from [Django REST framework](http://www.django-rest-framework.org/) viewsets.
    *  **[Django REST Swagger](https://github.com/marcgibbons/django-rest-swagger)** - This package is built on top of [Django REST framework](http://www.django-rest-framework.org/). It generates API documentation content based on the `docstring documentation`, `method arguments` etc in the viewsets,
    *  **[fake-factory](https://pypi.python.org/pypi/fake-factory)** - This API employs the use of this library in the unittests. It generates random values for input when testing.
    *  **[ipdb](https://pypi.python.org/pypi/ipdb)** - The Python debugger. Very useful during development.
    *  **[coverage](https://coverage.readthedocs.org/en/coverage-4.0.3/)** - This package is used to run tests and generate test coverage reports thereafter. It's output details the percentage of code (per file) that has been executed by the tests.

### Front End Dependencies
*  The front end heavily relies on JavaScript based frameworks including;
    * **[Angular JS](https://angularjs.org/)** - A Superheroic JavaScript MVC Framework. This API uses Angular JS to bind data from the front end to the controllers, to provide behaviour to view elements and to pass authentication tokens with every request sent after user login.
    * All this is accomplished mainly through two critical modules;
      *  **`angular-route`** - Used for single page applications and loads views along with their controllers depending on the current route on the front end
      *  **`angular-resource`** - Used to create resources that are used to interact with the REST endpoints at the back end.
    * **[Sweet Alert](http://t4t5.github.io/sweetalert/)** - A beautiful replacement for Javascript's "Alert" dialog. Used when the user is required to confirm delete operations on the front end.
    * **[Materialize CSS](http://materializecss.com/)** - The front end framework from which all the elements and controls on the front end have been created.

## Installation and Setup
*  Navigate to a directory of choice on `terminal`
*  Clone this repository on that directory.
  *  Using ssh;
    *  `git clone git@github.com:andela-lkabui/checkpoint3.git`
  *  Using http;
    *  `git clone https://github.com/andela-lkabui/checkpoint3.git`
* Navigate to the repo's folder
    *  `cd checkpoint3/`
*  Install the project's backend dependencies. For best results, using a [virtual environment](https://virtualenv.readthedocs.org/en/latest/) is recommended.
  *  `pip install -r requirements`
*  Install the project's database. **PostgreSQL** was used for this checkpoint. Locate your platform and follow the installation instructions [here](http://www.postgresql.org/download/)
*  Install the project's front end dependencies using [bower](http://bower.io/). First navigate to the project's root directory (where `bower.json` is located) and run the following command.
  *  `npm install bower`
  *  `./node_modules/bower/bin/bower install`


 ```Please note that in order to use bower, you need to have node, npm and git installed on your system```

*  After installation of the dependencies above, create a database on PostgreSQL for this app.
*  Set the environment variable **`DATABASE_URL`** with the **username**, **password**, **port** and **database name**. Refer to the structure of **`DATABASE_URL`** in the **Front End Dependencies** section above.
*  Create and apply migrations
  *  `python manage.py makemigrations api`
  *  `python manage.py migrate api`
*  Run the app
  *  `python manage.py runserver`
*  A message that's similar to the example below is displayed on terminal when the app starts running.


  ```
  System check identified no issues (0 silenced).
  February 17, 2016 - 15:58:14
  Django version 1.9.1, using settings 'checkpoint3.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
  ```

*  To start the app, visit the following url on a web browser.

  `http://localhost:8000`

## Routes, methods and functionality
*  To view this API's documentation, visit `/api/docs/` while the app is running and explore the resources and associated actions it has to offer.

## Tests
*  The tests have been written in classes that inherit [Django REST framework](http://www.django-rest-framework.org/)'s **`APITestCase`**.
*  The tests are run with the **`coverage`** package to facilitate the creation of test coverage reports.
*  To run the tests, first ensure you are in the project's root folder (where the file requirements.txt is located)
*  Issue the following command on terminal.
  *  `coverage run manage.py test`
*  The tests are successful if they run without failures or errors
  ```
  .....................................
  ----------------------------------------------------------------------
  Ran 37 tests in 3.384s

  OK
  ```
*  To view test coverage, run the following command.
  *  `coverage report -m`
  *  Below is a sample of the output.
  ```
  Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
api/__init__.py                                  0      0   100%
api/admin.py                                     4      0   100%
api/models.py                                   17      0   100%
api/paginator.py                                 5      0   100%
api/permissions.py                               9      1    89%   16
                    .
                    .
                    .
tests/test_user_login_and_logout.py              9      0   100%
--------------------------------------------------------------------------
TOTAL                                          757     10    99%
```

