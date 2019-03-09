from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/research_papers"
mongo = PyMongo(app)


@app.route('/')
def root_page():
        return 'List of Papers:</br>' + "</br>".join(x['Title'] for x in mongo.db.papers.find({}, {'Title': True, "_id": False}))


@app.route('/papers/<paper_id>')
def show_paper(paper_id):
    return "Showing Paper : " + paper_id


if __name__ == '__main__':
    app.run()
