# Dependencies 
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create instance of Flask app 
app = Flask(__name__)

# Connect to MongoDB 
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

# rout to display results
@app.route("/")
def home():
    
    mars_data = db.mars_db.find_one()

    # Render HTML template 
    return render_template("index.html", mars_data=mars_data)
#route to run scraping function
@app.route("/scrape")
def scrape(): 
    
    alldata = db.mars_db

    # run scrape function to get the data 
    mars_data = scrape_mars.scrape()

    # insert data to mars_db
    alldata.update({}, mars_data, upsert = True)


# Run the application
if __name__ == "__main__":
    app.run(debug=True)