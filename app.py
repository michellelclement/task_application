import os
from flask import Flask

#Create new instance of Flask app and store in variable app
app = Flask(__name__) 

@app.route('/') #/ refers to defult route
def hello():
    return 'Hello World... again'

#Set up IP address and port number so it knows where and how to run application
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

