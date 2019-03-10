from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from flask_pymongo import ObjectId
import json
from jinja2 import *


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/research_papers"
mongo = PyMongo(app)

@app.route('/')
def root_page():
  return 'List of Papers:</br>' + "</br>".join(x['Title'] for x in mongo.db.papers.find({}, {'Title': True, "_id": False}))



@app.route('/papers/<paper_id>/view')
def show_paper(paper_id):
    data = mongo.db.papers.find_one({'_id': ObjectId(paper_id)})
    print(data)
    return render_template('template_format.html', **data)


@app.route('/papers/<paper_id>/edit')
def edit_paper(paper_id):
    y = mongo.db.papers.find_one({'_id': ObjectId(paper_id)})

    return "test"

if __name__ == '__main__':
    app.run()
