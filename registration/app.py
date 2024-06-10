from flask import Flask ,render_template,request,redirect,session,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField ,Form, validators
from wtforms.fields import EmailField , PasswordField
from wtforms.validators import InputRequired, ValidationError,Email
from flask_login import LoginManager, login_user, login_required, logout_user, current_user,UserMixin
from sqlalchemy.orm import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SECRET_KEY'] = 'abc'
app.app_context().push()
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)


# create table
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def is_active(self):
        return True
    
    def get_id(self):
        return str(self.id)


# velidators
class Uservelidator(Form):
    username = StringField('username',validators=[InputRequired()])
    email = EmailField('email',validators=[InputRequired()])
    password = PasswordField('password',[validators.DataRequired(),validators.Length(min=8,max=12)])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
        
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email already in use.')
        
    def validate_password(self,field):
        password = field.data
        special_char = ['!','@','#','$','%','&']
        if not any(char.isdigit() for char in password):
            raise ValidationError('password has atlist one number')
        if not any(char.isupper() for char in password):
            raise ValidationError('password must be atlist one uppercase ')
        if not any(char.islower() for char in password):
            raise ValidationError('password must be atlist one lowercase')
        if not any(char in special_char for char in password):
            raise ValidationError('password must be atlist one special word between[!,@,#,$,%,&]')
        
class Userlogin(Form):
    email = EmailField('email',validators=[InputRequired()])
    password = PasswordField('password',[validators.DataRequired(),validators.Length(min=8,max=12)])
    

# index page
@app.route('/index')
def index():
    users = User.query.all() 
    return render_template('index.html',users=users)

# fatch one record
@app.route('/<int:user_id>/')
def user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('oneuser.html',user = user)


@app.route("/", methods=["GET", "POST"])
def login():
    form = Userlogin(request.form)
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash("Invalid Password !")
        else:
            if User.query.filter_by(password=password).first():
                flash("Invalid Email !")
            else:
                flash("check your email and password otherwise create user")

    return render_template("login.html", form=form)

@app.route('/register/',methods=('GET','POST'))
def register():
    form = Uservelidator(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username = username,email = email,password = password)
        db.session.add(user)
        db.session.commit()

        return redirect('/')
    
    return render_template('register.html',form = form)

def get_user_by_id(session: Session, user_id: int):
    return session.get(User, user_id)

@app.route('/home',methods=('GET', 'POST'))
@login_required
def home():
    form = Uservelidator(request.form)  # Initialize form object
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user.username = username
            user.email = email
            if password:
                user.password = password

            db.session.commit()
            flash('User details updated successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Form validation failed. Please check your input.', 'error')
    form.username.data = current_user
    form.email.data = current_user
    rows = User.query.all()

    return render_template('home.html', user=current_user, form=form , rows = rows)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('/'))

@app.route('/update_user', methods=['POST'])
@login_required
def update_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Update the user's data in the database
        user = current_user
        user.username = username
        user.email = email
        user.password = password
        db.session.commit()
        
        flash('User details updated successfully!', 'success')
    
    # Redirect to the home page or refresh the page to reflect changes
    return redirect(url_for('home'))


@app.route('/delete',methods=['POST'])
@login_required
def delete():
    if request.method == 'POST':
        user = current_user
        db.session.delete(user)
        db.session.commit()

        flash('User has Delete successfully','success')

        return redirect('register')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)