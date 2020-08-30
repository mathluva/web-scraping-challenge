from flask import Flask, render_template, redirect

from flask_pymongo import PyMongo

import pymongo

import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#mongo = PyMongo(app, uri="mongodb://localhost:27017")
conn = 'mongodb://localhost:27017'
client =pymongo.MongoClient(conn)

db = client.mars_db

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    scrape = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, scrape, upsert=True)

    # Redirect back to home page
    return redirect("/")
'''
def index():
    # Store the entire team collection in a list
    teams = list(db.team.find())
    print(teams)

    # Return the template with the teams list passed in
    return render_template('index.html', teams=teams)

'''

if __name__ == "__main__":
    app.run(debug=True)
