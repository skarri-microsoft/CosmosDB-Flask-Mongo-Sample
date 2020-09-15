from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "TODO with Flask"
heading = "ToDo Reminder"

@app.route("/")
	return "Hello World!"

# define for IIS module registration.

wsgi_app = app.wsgi_app

if __name__ == "__main__":

    app.run()




