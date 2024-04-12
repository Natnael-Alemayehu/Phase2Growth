from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/airtable')
def hello_world():
    message = "This is from the airtable route!"
    import deployment_test
    return message