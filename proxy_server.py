from flask import Flask, request, Response, abort
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

TARGET_SERVER = 'https://hc-ping.com'  
VALID_API_KEYS = os.getenv('VALID_API_KEYS').split(',')

@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    auth_key = request.args.get('auth_key')    
    
    if auth_key not in VALID_API_KEYS:
        abort(403)  # Forbidden if the API key is invalid
    
    # Build the target URL
    target_url = f'{TARGET_SERVER}/{path}'
    
    # Forward the GET request to the target server
    response = requests.get(target_url)
    
    # Return the response from the target server unchanged
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

if __name__ == '__main__':
    #app.run(debug=True, port=3452)
    #app.run(debug=True, host='0.0.0.0', port=3452)
    app.run()