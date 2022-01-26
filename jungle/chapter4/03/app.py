from pymongo import MongoClient

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

client = MongoClient('localhost',27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/api/list', methods=['get'])
def show_stars():
    result = list(db.mystar.find({},{'_id' : 0}).sort('like',-1))
    # print(result)
    return jsonify({'result' : 'success' , 'movie_stars': result})


@app.route('/api/like' ,methods=['post'])
def like_stars():
    name_recieve = request.form['name_give']
    star = db.mystar.find_one({'name' : name_recieve})
    db.mystar.update_one({'name':name_recieve},{'$set' :{'like': star['like']+1}})
    return jsonify({'result': 'success','msg':'좋아요 완료'})


@app.route('/api/delete', methods = ['post'])
def delete_stars():
    name = request.form['name']
    db.mystar.delete_one({'name':name})
    return jsonify({'result': 'success','msg':'삭제 완료'})

if __name__ == '__main__' :
    app.run('0.0.0.0',port=5000 , debug=True)