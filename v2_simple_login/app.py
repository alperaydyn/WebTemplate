import os
from flask import Flask, render_template, render_template_string, jsonify
import teknokent_scraper as tns

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# login ---------------------------------------------------------------------------------
# https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask-login/

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"
db = SQLAlchemy()
 
login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
 
 
db.init_app(app) 
with app.app_context():
    db.create_all()
    
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)    

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if isinstance(user, type(None)):
            user = Users(username=request.form.get("username"),
                         password=request.form.get("password"))
            db.session.add(user)
            db.session.commit()
            return render_template("sign.html", method="login", message="Username successfully created, please login")
        else:
            return render_template("sign.html", method="register", message="User already exists")
            
    return render_template("sign.html", method="register")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form.get("username")).first()
        if isinstance(user, type(None)):
            return render_template("sign.html", method="login", message="User not found")
        else:
            if user.password == request.form.get("password"):
                login_user(user, remember=False)
                #return redirect(url_for("home"))
                return render_template("sign.html", method="logged-in", message="Login successfull", 
                                       redirect_to=url_for('home'))
            else:
                return render_template("sign.html", method="login", message="Username or Password not correct")
            
    return render_template("sign.html", method="login")
    
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
 
@app.route("/forgot_password")
def forgot_password():
    return render_template("sign.html", method="forgot_password")

@app.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        username = request.form.get("username")
        user = Users.query.filter_by(username=username).first()
        if isinstance(user, type(None)):
            return render_template("sign.html", method="forgot_password", message=f"User `{username}` not found")
        else:
            return render_template("sign.html", method="reset_password", message="<h3 style='color:red'>please contact to admin</h3>")
        
    return render_template("sign.html", method="reset_password")

@app.route("/")
def home():
    return render_template("home.html")

# /login ---------------------------------------------------------------------------------

# universal function to call pages without explicit routing but having template files
@app.errorhandler(404)
def not_found(e):
    url = request.path
    try:
        return render_template(f'{url}.html')
    except:
        return render_template('error404.html', url=url)

# ---------------------------------------------------------------------------------




@app.route('/')
def init():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
