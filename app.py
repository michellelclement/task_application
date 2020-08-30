import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

#Create new instance of Flask app and store in variable app
app = Flask(__name__) 

#Link to MongoDB Database
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:R00tUser@myfirstcluster.visoz.mongodb.net/task_manager?retryWrites=true&w=majority'

#Create an instance of PyMongo
mongo = PyMongo(app)

@app.route('/') #/ refers to defult route
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


#Set up IP address and port number so it knows where and how to run application
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

