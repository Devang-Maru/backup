from flask import Flask,render_template,request,flash
import sqlite3

app = Flask(__name__)
app.secret_key="ABC"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('register.html')

@app.route('/access')
def access():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

# register page
@app.route('/register',methods=['GET','POST'])
def register():
    msg = "msg"
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            with sqlite3.connect("Emp.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT into employes (name,email,password) values(?,?,?)",(name,email,password))
                conn.commit()
        except:
            conn.rollback()
            msg = "we are sorry data has not recorded"

        finally:
            return render_template('login.html')
            conn.close()
    
# login page 
@app.route('/login',methods=['GET','POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    conn = sqlite3.connect("Emp.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("select * from employes where email = '"+email+"' and password = '"+password+"'")
    rows = cur.fetchall()

    return render_template("home.html",rows = rows)

#view data
@app.route('/view')
def viewdata():
    conn = sqlite3.connect("Emp.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from employes")
    rows = cur.fetchall()

    return render_template("viewdata.html",rows = rows)



if __name__ == "__main__":
    app.run(debug=True)
