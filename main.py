from flask import Flask,jsonify,request
import csv
from demographic_filtering import output
from content_filtering import get_recommendations

all_articles=[]
with open ("articles.csv") as f:
    r=csv.reader(f)
    data=list(r)
    all_articles=data[1:]
    liked_articles=[]    
    not_liked_articles=[]
app=Flask(__name__)

@app.route("/get-article")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked-article",methods=["POST"])
def liked_article():
    article=all_articles[0],
    all_articles=all_articles[1:]
    liked_article.append(article)
    return jsonify({
        "status":"success"
    }),201
@app.route("/popular-movies")
def popular_articles():
    article_data = []
    for recommended in output:
        _d = {
         "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2] ,
            "lang": recommended[3],
            "total_events": recommended[4],   
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200    

@app.route("/unliked-article",methods=["POST"])
def unliked_article():
    article=all_articles[0],
    all_articles=all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201 
@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[4])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    movie_data = []
    for recommended in all_recommended:
        _d = {
            "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2] ,
            "lang": recommended[3],
            "total_events": recommended[4],
            
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200


if __name__=="__main__":
    app.run()