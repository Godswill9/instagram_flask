# from flask import Flask, request, jsonify
# from flask_cors import CORS 
# # from bs4 import BeautifulSoup
# import requests

# app = Flask(__name__)

# allowed_origins = [
#     "http://127.0.0.1:5500",
#     "https://simple-insta-download.netlify.app"
# ]

# CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

# @app.route('/', methods=['GET'])
# def index():
#     return 'Welcome to my Flask App from python!'

# @app.route('/api/downloadFile', methods=['POST'])
# def receive_url():
#     if request.method == 'POST':
#         data = request.get_json()
#         if 'url' in data:
#             url = data['url']
#             print(url)
#             try:
#                 # Fetch the HTML content from the URL
#                 response = requests.get(url)
#                 print(response)
#                 if response.status_code == 200:
#                     parsedData = response.content  # Send the entire HTML content back as parsedData
#                     return parsedData
#                 else:
#                     return jsonify({'error': 'Failed to fetch URL'})
#             except Exception as e:
#                 return jsonify({'error': str(e)})
#         else:
#             return jsonify({'error': 'URL not found in request'})
#     else:
#         return jsonify({'error': 'Invalid request method'})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

allowed_origins = [
    "http://127.0.0.1:5500",
    "https://simple-insta-download.netlify.app"
]

CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to my Flask App from python!'

@app.route('/api/downloadFile', methods=['POST'])
def receive_url():
    if request.method == 'POST':
        data = request.get_json()
        if 'url' in data:
            url = data['url']
            print(url)
            try:
                # Set up a headless browser using Selenium
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')  # Run browser in headless mode
                driver = webdriver.Chrome(options=options)

                # Open the URL in the browser
                driver.get(url)

                # Get the rendered HTML content after JavaScript execution
                html_content = driver.page_source

                # Use BeautifulSoup to parse the HTML content
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Find the <pre> tag and extract its content
                pre_tag = soup.find('pre')
                if pre_tag:
                    pre_content = pre_tag.get_text()
                    # Try parsing content inside <pre> tag as JSON
                    try:
                        json_data = json.loads(pre_content)
                        return jsonify(json_data)
                    except json.JSONDecodeError:
                        return jsonify({'error': 'Content inside <pre> tag is not valid JSON'})
                else:
                    return jsonify({'error': 'No <pre> tag found'})
            except Exception as e:
                return jsonify({'error': str(e)})
            finally:
                # Close the browser when done
                driver.quit()
        else:
            return jsonify({'error': 'URL not found in request'})
    else:
        return jsonify({'error': 'Invalid request method'})

if __name__ == '__main__':
    app.run(debug=True)
