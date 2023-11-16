from flask import Flask, request, jsonify
from flask_cors import CORS 
from my_spider import run_spider  # Importing the function from your Scrapy file



app = Flask(__name__)
allowed_origins = [
    "http://127.0.0.1:5500",  # First origin
    "https://simple-insta-download.netlify.app"     # Yet another origin (example)
]

CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to my Flask App!'

@app.route('/api/downloadFile2', methods=['POST'])
def receive_url():
    if request.method == 'POST':
        data = request.get_json()
        if 'url' in data:
            url = data['url']
            print(url)
            try:
                run_spider(url)  # Run the Scrapy spider
                # Read the scraped HTML content from the output file
                with open('output.json', 'r') as file:
                    scraped_data = file.read()
                return scraped_data  # Send the scraped HTML content back to the client
            except Exception as e:
                return jsonify({'error': str(e)})
        else:
            return jsonify({'error': 'URL not found in request'})
    else:
        return jsonify({'error': 'Invalid request method'})

if __name__ == '__main__':
    app.run(debug=True)