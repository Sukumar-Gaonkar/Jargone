from flask import Flask
from flask_pymongo import PyMongo
from flask_pymongo import ObjectId


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/research_papers"
mongo = PyMongo(app)

@app.route('/')
def root_page():
    return """
        <h1>Hello world!</h1>

        <iframe src="https://www.youtube.com/embed/YQHsXMglC9A"
         width="853" height="480" frameborder="0"
         allowfullscreen></iframe>
        """
        # return 'List of Papers:</br>' + "</br>".join(x['Title'] for x in mongo.db.papers.find({}, {'Title': True, "_id": False}))


@app.route('/papers/<paper_id>/view')
def show_paper(paper_id):
    id = paper_id
    y = mongo.db.papers.find_one({'_id': ObjectId(paper_id)})
    return y['video_link']

@app.route('/papers/<paper_id>/edit')
def edit_paper(paper_id):
    # return "Showing Paper : " + paper_id

if __name__ == '__main__':
    app.run()
