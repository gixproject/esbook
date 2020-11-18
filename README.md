# ESbook

## Basics
The REST API platform that provides search within millions of books.  
API represents results in a suitable JSON format that can be helpful to other developers and sales companies.  
The functionality allows you to retrieve data for a period or just by one author. 
Periodical updates help to keep the data fresh. API uses the Python programming language as the ideal solution for processing, parsing, updating a big amount of data.

## Configuration
Run the project in four simple steps:
1. Copy `.env.dist` file content to `.env`
2. Build the project `docker-compose build`
3. Run the project `docker-compose up`
4. Open `localhost:5000`

Pay attention that database setting already has defaults values.

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
