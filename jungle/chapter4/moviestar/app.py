from http import client
from pymongo import MongoClient

from flask import Flask, redirect , render_template , jsonify , request


app = Flask(__name__)

# client = MongoClient('localhost',27017)
# client = MongoClient('mongodb://test:test@localhost',27017)
client = MongoClient('mongodb://connie:1234@13.209.19.241',27017)
db = client.geonhee


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list')
def show_list():
    movie_list = list(db.movies.find({}, {'_id' : False}).sort('like',-1))
    return jsonify({'movies' : movie_list})


@app.route('/api/like' , methods = ['post'])
def like_star() :
    name = request.form['name']
    star = db.movies.find_one({'name' : name})
    db.movies.update_one({'name':name}, {'$set' : {'like' : star['like']+1}})
    return jsonify({'msg' :'좋아요 완료'})


@app.route('/api/delete' ,methods=['post'])
def delete_star() :
    name = request.form['name']
    db.movies.delete_one({'name':name})
    return jsonify({'msg' :'삭제 완료' })


@app.route('/api/post', methods=['POST'])
def post_star():
    name = request.form['nameReceiver']
    recent = request.form['recentReceiver']
    url = request.form['urlReceiver']
    db.movies.insert_one({'name' :name , 'recent_work' : recent , 'image_url' : url , 'like' :0})
    return jsonify({'msg' :'등록 완료' })
    # return render_template('index.html')



        

@app.route('/api/page', methods=['GET'])
def post_page():  
    return render_template('post.html')


if __name__ == '__main__' :
    app.run('0.0.0.0',port=5000 , debug=True)