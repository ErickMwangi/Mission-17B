from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User  

app = Flask(__name__)
CORS(app)

# Database setup
DATABASE_URL = 'sqlite:///app.db'
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

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
    session = SessionLocal()
    try:
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        session.add(new_user)
        session.commit()
        return jsonify({"status": "success", "user_id": new_user.id}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 400
    finally:
        session.close()


@app.route('/api/users', methods=['GET'])
def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return jsonify([
        {"id": user.id, "username": user.username, "email": user.email}
        for user in users
    ])

if __name__ == '__main__':
    app.run(port=5000, debug=True)
