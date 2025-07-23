from flask import Flask, request
from flask_bootstrap import Bootstrap4
from generate_pass import generate_passphrase

app = Flask(__name__)
Bootstrap4(app)

@app.route('/')
def home():
    """
    Default route when visiting /
    
    Returns:
        Result of generate_passphrase
    """
    passphrase = generate_passphrase() + "\n"
    return passphrase

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
