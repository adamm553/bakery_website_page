from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "whooy"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=3)

db = SQLAlchemy(app)
app.app_context().push()

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
        flash("Zalogowano")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Jesteś juz zalogowany")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=['POST', 'GET'])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form['email']
            session['email'] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Zapisano e-mail!")
        else:
            if 'email' in session: 
                email = session['email']

        return render_template("user.html", email=email)
    else:
        flash("Nie jesteś zalogowany!")
        return redirect(url_for("login"))
    
@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/memes")
def memes():
    return render_template("memes.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/gracias")
def gracias():
    return render_template("gracias.html")

@app.route("/rating")
def rating():
    return render_template("rating.html")
    
@app.route("/logout")
def logout():
    flash(f"Zostałeś wylogowany", "info")
    session.pop("user", None)
    session.pop('email', None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run()