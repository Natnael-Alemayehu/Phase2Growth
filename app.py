from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/airtable')
def testing_path():
    message = "This is from the airtable route!"
    import deployment_test
    return message