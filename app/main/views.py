from app import app,db
from flask import render_template,redirect,url_for
from flask_login import login_required,login_user,current_user,logout_user
from .forms import LoginForm,RegisterForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))


    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))


    return render_template('signup.html', form=form)




@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/fruits')

def fruits():

    return render_template('fruits.html')


@app.route('/kitchen')

def kitchen():

    return render_template('kitchenhad.html')
