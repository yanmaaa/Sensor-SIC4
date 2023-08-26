from pymongo import MongoClient
from flask import Flask, render_template

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['nama_database']
collection = db['data_collection']
data = collection.find()

@app.route('/')
def show_data():
    data = collection.find()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)