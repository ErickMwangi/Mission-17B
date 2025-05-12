from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

content_data = {
    "hero": "Welcome to Mission 17B",
    "hero_desc": "Stay tuned for something amazing!",
    "content": "Stay informed with partnership news, updates, and stories from the young people driving social change.",
    "thank_you": "Thank you for your patience and support!"
}


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
    data = request.json
    print("Received contact data:", data)
    return jsonify({"status": "success", "message": "Contact data received"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
