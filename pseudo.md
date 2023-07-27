# What am I doing?
- I really am not sure. I am on the island from Castaway with a bunch of sharks out in the sea wherever I look.

# Requirements/Rubric
For this project, we will be creating a simple Python/Django API to serve as the backend for our previously created React Restaurant frontend app. 
Create the models, views, and database for an API that provides READ operations for a user’s restaurant items in a PostgresQL database. 
The app should be able to perform READ ONLY operations on the Restaurant models as well as have routes to display information as JSON.
## Tech Stack
- Python/Django
- PostgreSQL
- ThunderClient/Database Client (VS Code Extensions)
- JS/React
## Process
### Setup
- Pseudocode your project by determining your end-points and database schema
- Create GitHub repo online
- Save all and create your first commit to main, then switch to a dev branch

# Procedural

## Begin:
- Setup: Install Django and required dependencies, create a new Django project, and configure the database settings to use PostgresQL.

- Define Models: Create the necessary models to represent restaurant items, such as Category and MenuItem. Each model should have relevant fields like name, description, price, etc.
## Init:
- Create the API with the table
- Create Views: Implement API views to handle READ operations (GET requests) for the restaurant items. These views will be responsible for fetching data from the database.

- Create URLs: Define URLs and URL routing for the API views. This will determine the endpoints through which the frontend can access the data.
- Install Django Dependencies: Install the required Python packages, including Django and other dependencies.

- Create Django Project: Set up a new Django project using the django-admin or manage.py command.

- Configure Database: Specify the settings for connecting the Django project to a PostgresQL database or any other desired database.

- Define Models: Create the Django models that will represent the Category and MenuItem entities for the restaurant menu.

- Create API Views: Define Django views that handle the READ operations for the restaurant items.

- Create API URLs: Create URL patterns for the API views to define their endpoints.

## Render: 
send the data over to the React components
# Functional

# Object Oriented
```
class menu item{
name: string
id: integer
spice: string
description: string
cuisine_id: int
location_id: int
}

```
# GPT advice 
## Begin:
- Setup: Install Django and required dependencies, create a new Django project, and configure the database settings to use PostgresQL.

- Define Models: Create the necessary models to represent restaurant items, such as Category and MenuItem. Each model should have relevant fields like name, description, price, etc.

- Create Views: Implement API views to handle READ operations (GET requests) for the restaurant items. These views will be responsible for fetching data from the database.

- Create URLs: Define URLs and URL routing for the API views. This will determine the endpoints through which the frontend can access the data.

Database Setup and Migrations: Set up the database tables based on the defined models. Run migrations to create the tables and ensure database schema is in sync with the models.

Configure Serializers: Create serializers to convert the model instances into JSON data and vice versa. These serializers will help in presenting the data over the API.

View Functions Implementation: Implement view functions for each API view. These functions will fetch data from the database using Django's ORM and serialize it using the previously created serializers.

API Documentation: Generate API documentation using DRF-YASG or a similar library. Include relevant information about the endpoints, request/response formats, and authentication.

Test the API: Start the development server and test the API endpoints. Ensure that the API returns the expected data and handles errors gracefully.

Integration with React Frontend: Update the frontend app to make API calls to the created backend API for fetching restaurant items. Ensure that the frontend can correctly consume the data from the backend.

Deployment: Prepare the application for deployment to a production environment. Configure necessary settings for production, including database connection, static files, and security settings.

## Initialize:
Install Django Dependencies: Install the required Python packages, including Django and other dependencies.

Create Django Project: Set up a new Django project using the django-admin or manage.py command.

Configure Database: Specify the settings for connecting the Django project to a PostgresQL database or any other desired database.

Define Models: Create the Django models that will represent the Category and MenuItem entities for the restaurant menu.

Create API Views: Define Django views that handle the READ operations for the restaurant items.

Create API URLs: Create URL patterns for the API views to define their endpoints.

Database Setup and Migrations: Apply the migrations to set up the database tables based on the defined models.

Configure Serializers: Implement serializers to convert model instances to JSON data.

Implement View Functions: Write functions for the API views to fetch data from the database and serialize it using the serializers.

Generate API Documentation: Use DRF-YASG or similar tools to generate API documentation for the created endpoints.

Test the API: Start the development server and test the API endpoints to ensure they function correctly.

Update Frontend App: Integrate the backend API into the React frontend app to fetch restaurant items from the backend.

Prepare for Production: Get the application ready for deployment in a production environment.

Configure Production Settings: Adjust settings, such as database connection, security, and static file handling, for the production deployment.
