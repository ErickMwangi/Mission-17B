from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import User 

app = Flask(__name__)
CORS(app)

# Set database URI for Flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

content_data = {
    "hero": "Welcome to Mission 17B",
    "hero_desc": "Stay tuned for something amazing!",
    "content": "Stay informed with partnership news, updates, and stories from the young people driving social change.",
    "thank_you": "Thank you for your patience and support!"
}

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hero')
def get_hero():
    return jsonify({
        "title": content_data["hero"],
        "description": content_data["hero_desc"]
    })

@app.route('/api/content')
def get_content():
    return jsonify({
        "contentText": content_data["content"]
    })

@app.route('/api/thankyou')
def get_thank_you():
    return jsonify({
        "thankYouText": content_data["thank_you"]
    })

@app.route('/api/contact', methods=['POST'])
def contact():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    print("Received contact data:", data)
    return jsonify({"status": "success", "message": "Contact data received"}), 200

# Create a user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    try:
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"status": "success", "user_id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 400

# List all users
@app.route('/api/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([
        {"id": user.id, "username": user.username, "email": user.email}
        for user in users
    ])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
