# pizza-api-challenge
A RESTful API for managing pizza restaurants, their menus, and pizza associations, built with Flask and SQLAlchemy following MVC pattern.

## Features

- RESTful endpoints for restaurants, pizzas, and restaurant-pizza relationships
- Proper MVC architecture (Models, Views/Controllers, Configuration)
- Database migrations with Flask-Migrate
- SQLAlchemy for ORM
- Ready-to-use Postman collection for testing

## Project Structure
pizza-api-challenge/
├── server/
│ ├── init.py # App factory
│ ├── app.py # Main application entry
│ ├── config.py # Configuration settings
│ ├── models/ # Database models
│ │ ├── init.py
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ ├── controllers/ # Route handlers
│ │ ├── init.py
│ │ ├── restaurant_controller.py
│ │ ├── pizza_controller.py
│ │ └── restaurant_pizza_controller.py
│ └── seed.py # Database seeder
├── migrations/ # Database migration files
├── challenge-1-pizzas.postman_collection.json # Postman collection
└── README.md # This file

text

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/almasi89/pizza-api-challenge.git
   cd pizza-api-challenge
Create virtual environment

    python -m venv venv


Install dependencies

    pip install -r requirements.txt
    Database Setup

Database setup

    export FLASK_APP=server.app
    flask db init
    flask db migrate -m "Initial tables"
    flask db upgrade
    Seed the database

seed database

    python server/seed.py

Run the application

    flask run

API Endpoints

    Restaurants
        GET /restaurants - List all restaurants

        GET /restaurants/<int:id> - Get specific restaurant

        DELETE /restaurants/<int:id> - Delete a restaurant

        POST /restaurants - Create new restaurant

Pizzas
    GET /pizzas - List all pizzas

    GET /pizzas/<int:id> - Get specific pizza

RestaurantPizzas
    POST /restaurant_pizzas - Create pizza association

