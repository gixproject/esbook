# ESbook

## Basics
The REST API service that provides search within millions of books.  
API represents results in a suitable JSON format that can be helpful to other developers and sales companies.  
The functionality allows you to retrieve data for a period or just by one author. 
Periodical updates help to keep the data fresh. API uses the Python programming language as the ideal solution for processing, parsing, updating a big amount of data.

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
Configure the project with test data:  
`docker-compose exec web python manage.py apply_test_data`  

Migrate existing books to ElasticSearch:  
`docker-compose exec web python manage.py migrate_books_to_es`  

### Make commands support
For details type `make help`  

### Testing
Run tests `make test`  
Run lint `make lint`

## Additional info
#### Libraries and tools
* Docker + compose
* Poetry package manager
* Flask Framework
* Flask-restplus
* PostgreSQL
* SQLAlchemy
* ElasticSearch
* unittest + pytest
* invoke
