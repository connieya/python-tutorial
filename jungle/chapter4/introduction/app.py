from flask  import Flask , render_template
from falsk_sqlalchemy import SQLAlchemu
app = Flask(__name__)
app.debug = True
app.config['SQLALCHMY_DATABASE_URI'] = 'sqllite:///test.db'
db = SQLAlchemu(app)
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__" :
    app.run(debug=True)