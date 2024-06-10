from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdb.db'
app.config['SECRET_KEY'] = 'hello_user'
app.app_context().push()
db = SQLAlchemy(app)

# create table


#index file
@app.route('/')
def index():
    return render_template('index.html')


#user file
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',user_name=name)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)