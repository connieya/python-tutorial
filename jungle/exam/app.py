from http import client
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, redirect,render_template , jsonify , request , flash


app = Flask(__name__)
app.secret_key = 'geonhee'
client = MongoClient('localhost',27017)
db = client.jungleExam



@app.route('/')
def home():
    memo_list = list(db.memo.find({}))
    print(memo_list)
    return render_template('index.html',memo_list=memo_list)


@app.route('/register', methods=['POST'])
def post_memo():
    data = request.form
    title = data['title']
    content = data['content']
    db.memo.insert_one({'title' : title, 'content': content})
    flash("저장 완료!")
    return redirect('/')


@app.route('/delete' ,methods=['post'])
def delete_memo() :
    _id = request.form['_id']
    db.memo.delete_one({'_id': ObjectId(_id)})
    return jsonify({'msg' :'삭제 완료!' })

@app.route('/edit/<pk>' ,methods=['get'])
def update_form(pk) :
    original = db.memo.find_one({'_id':ObjectId(pk)})
    return render_template('edit.html' , original = original)


@app.route('/update' ,methods=['post'])
def update_memo() :
    newTitle = request.form['newTitle']
    newContent = request.form['newContent']
    pk_key = request.form['id']
    print("tqdsadas",newTitle,newContent,pk_key)
    original = db.memo.find_one({'_id':ObjectId(pk_key)})
    db.memo.update_one({'_id': ObjectId(original['_id'])},{'$set':{'title':newTitle , 'content' :newContent}})
    return jsonify({'msg' :'수정 완료!' })


if __name__ == '__main__' :
    app.run('0.0.0.0',port=5000 , debug=True)