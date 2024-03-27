from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, People, Planets, Favorites, User

app = Flask(__name__)

# Create database engine
engine = create_engine('sqlite:///starwars.db')

# Bind the engine to the metadata of the Base class
Base.metadata.bind = engine

# Create a session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Define API endpoints
@app.route('/people', methods=['GET'])
def get_people():
    people = session.query(People).all()
    return jsonify([person.serialize() for person in people])

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = session.query(People).filter_by(id=people_id).first()
    if person:
        return jsonify(person.serialize())
    else:
        return jsonify({'message': 'Person not found'}), 404

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = session.query(Planets).all()
    return jsonify([planet.serialize() for planet in planets])

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = session.query(Planets).filter_by(id=planet_id).first()
    if planet:
        return jsonify(planet.serialize())
    else:
        return jsonify({'message': 'Planet not found'}), 404

@app.route('/users', methods=['GET'])
def get_users():
    users = session.query(User).all()
    return jsonify([user.serialize() for user in users])

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    # Assume user_id is retrieved from session or JWT token
    user_id = 1  # Example user_id
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        favorites = session.query(Favorites).filter_by(user_id=user_id).all()
        return jsonify([favorite.serialize() for favorite in favorites])
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    # Assume user_id is retrieved from session or JWT token
    user_id = 1  # Example user_id
    favorite = Favorites(user_id=user_id, planet_id=planet_id)
    session.add(favorite)
    session.commit()
    return jsonify({'message': 'Favorite planet added successfully'}), 201

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):

    user_id = 1  # Example user_id
    favorite = Favorites(user_id=user_id, people_id=people_id)
    session.add(favorite)
    session.commit()
    return jsonify({'message': 'Favorite people added successfully'}), 201

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
  
