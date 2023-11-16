from flask import Flask, request, jsonify
from flask_cors import CORS 
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

allowed_origins = [
    "http://127.0.0.1:5500",
    "https://simple-insta-download.netlify.app"
]

CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to my Flask App!'

@app.route('/api/downloadFile', methods=['POST'])
def receive_url():
    if request.method == 'POST':
        data = request.get_json()
        if 'url' in data:
            url = data['url']
            print(url)
            try:
                # Fetch the HTML content from the URL
                response = requests.get(url)
                print(response)
                if response.status_code == 200:
                    parsedData = response.content  # Send the entire HTML content back as parsedData
                    return parsedData
                else:
                    return jsonify({'error': 'Failed to fetch URL'})
            except Exception as e:
                return jsonify({'error': str(e)})
        else:
            return jsonify({'error': 'URL not found in request'})
    else:
        return jsonify({'error': 'Invalid request method'})

if __name__ == '__main__':
    app.run(debug=True)
