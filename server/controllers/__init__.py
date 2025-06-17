from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        # Import models here to ensure they're registered with SQLAlchemy
        from .models.restaurant import Restaurant
        from .models.pizza import Pizza
        from .models.restaurant_pizza import RestaurantPizza
        
        # Create tables
        db.create_all()
    
    return app