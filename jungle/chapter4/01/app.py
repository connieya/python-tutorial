from urllib import request
from flask import Flask, jsonify , render_template
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return "This is My Page!"


@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/test',methods = ['GET'])
def test_get():
   title_receive = request.args.get('title-give')
   print(title_receive)
   return jsonify({'result' : 'success', 'msg' :'이 요청은 get!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)