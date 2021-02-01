# ESbook

[![Build Status](https://travis-ci.org/gixproject/esbook.svg)](https://travis-ci.org/gixproject/esbook)
[![Coverage Status](https://coveralls.io/repos/github/gixproject/esbook/badge.svg)](https://coveralls.io/github/gixproject/esbook)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Description
The boilerplate Flask application that provides search within books.

The API represents results in a suitable JSON format that can be helpful to other developers and companies.  
It allows you to retrieve data for a period or just by one author. 
Periodical updates help to keep the data fresh.  

### Libraries and tools
* Docker + compose
* Poetry package manager
* Flask Framework
* Flask-restplus
* PostgreSQL
* SQLAlchemy
* ElasticSearch
* gunicorn 
* unittest + pytest
* invoke

## Setup
Make sure **Docker** is installed on your system

Run the project in four simple steps:
1. Copy `.env.dist` file content to `.env`
2. Build the project `docker-compose build`
3. Run the project `docker-compose up`
4. Open `localhost:5000`

Pay attention that the config file already has defaults values

## Useful actions
### Commands
**To run commands use** `docker-compose exec web` to execute environment  
To see all commands type `python manage.py`  

Configure the project with test data:  
`manage.py apply_test_data`

Migrate existing books to ElasticSearch:  
`python manage.py migrate_books_to_es`

To see all URL's:  
`python manage.py show_urls`

To recreate database schema use:  
`python manage.py reset_db`

### Make commands support
For details type `make help`  

### Testing
Run tests `make test`  
Run lint `make lint`
