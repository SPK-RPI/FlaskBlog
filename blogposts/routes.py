from flask import render_template, url_for, flash, redirect
from blogposts.models import User, Post
from blogposts.forms import RegistrationForm, LoginForm
from blogposts import app, db, bcript
from flask_login import login_user

posts = [{
    'name': 'Shiva',
    'date_posted': 20190213,
    'author': 'sredhangali',
    'content': 'i ama a name of the '

}, {
    'name': 'Himesh',
    'date_posted': 20180213,
    'author': 'srikanta',
    'content': 'this is a test done to get'

}]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcript.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created !!,You are able to Log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title=' Register', form=form)


@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcript.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Login Unsucessful. Please check email and password..', 'success')
            return redirect(url_for('home'))

        else:
            flash(f'Login Unsucessful. Please check email and password..', 'success')
    return render_template('login.html', title=' Login', form=form)
