from flask import Flask, request, render_template, redirect, url_for, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from table_creation import create_table
from table_creation import Account, Post
from table_creation import db as db
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from auth_middleware import token_required
import jwt


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/postgres"
app.config['JWT_SECRET_KEY'] = "somerandomstring"
app.config['JWT_ALGORITHM'] = 'HS256'
db.init_app(app)

post_db = Post()

create_table(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    
    if not Account.query.filter_by(username=username).first():
    
        senha_hash = generate_password_hash(password, method="pbkdf2")

        new_user = Account(username=username, password=senha_hash)
        db.session.add(new_user)
        db.session.commit()
        return redirect("http://localhost:5000/") 
    else:
        return "Invalid Credentials", 401

@app.route('/login_user', methods=['POST'])
def login_user():
    username_login = request.form['username']
    password_login = request.form['password']

    user = Account.query.filter_by(username=username_login).first()

    if user and check_password_hash(user.password, password_login):
        try:
            # token should expire after 24 hrs
            key = "somerandomstring"
            user_token = jwt.encode({"user_id": str(user.id)}, key, algorithm="HS256")

            # Armazenar o token em um cookie seguro
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('user_id', str(user.id), httponly=True, secure=True)
            response.set_cookie('auth_token', user_token, httponly=True, secure=True)  # httponly=True para proteção contra ataques XSS


            return response

        except Exception as e:
                return {
                    "error": "Deu errado familia",
                    "message": str(e)
                }, 500
    else:
        return "Credenciais inválidas", 401


@app.route('/dashboard')
@token_required
def dashboard(current_user):
    jsonify(current_user)
    posts = Post.query.all()
    return render_template('dashboard.html', posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    post_title = request.form['post_title']
    post_text = request.form['post_content']
    
    new_post = Post(post_title=post_title, post_text=post_text)
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(url_for('dashboard'))

@app.route('/postpublish')
@token_required
def postpublish(current_user):
    jsonify(current_user)
    return render_template('postpublish.html')

@app.route('/sign_out', methods=["GET"])
def signout():

    response = make_response(redirect('http://localhost:5000/'))
    response.delete_cookie('user_id')
    response.delete_cookie('auth_token')
    
    return response

app.run(debug=True)