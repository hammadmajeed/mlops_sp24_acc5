import os
import pymongo
from flask import Flask, render_template

app = Flask(__name__)

def get_rows(database_name, collection_name, auth_source):
    # Retrieve username and password from environment variables
    username = os.environ.get('MONGODB_USERNAME')
    password = os.environ.get('MONGODB_PASSWORD')

    if not username or not password:
        raise ValueError("MongoDB username or password not provided in environment variables")

    # MongoDB connection URI with authentication
    uri = f"mongodb://{username}:{password}@mongodb:27017/?{auth_source}"

    # Connect to MongoDB
    client = pymongo.MongoClient(uri)
    print(client);
    # Select database
    db = client[database_name]

    # Select collection
    collection = db[collection_name]

    # List all documents in the collection
    documents = [doc for doc in collection.find()]
    return documents

@app.route('/')
def index():
    try:
        database_name = "my_db"  # Change this to your actual database name
        collection_name = "my_collection"  # Change this to your actual collection name
        auth_source = "authSource=admin"  # Change this to your MongoDB authentication database
        rows = get_rows(database_name, collection_name, auth_source)
        print(rows)
        return render_template('index.html', rows=rows)
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
