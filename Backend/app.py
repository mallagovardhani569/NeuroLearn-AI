from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        department = request.form["department"]
        year = request.form["year"]

        connection = sqlite3.connect("neurolearn.db")
        cursor = connection.cursor()

        try:
            cursor.execute("""
            INSERT INTO students(name,email,password,department,year)
            VALUES(?,?,?,?,?)
            """, (name, email, password, department, year))

            connection.commit()

        except sqlite3.IntegrityError:
            connection.close()
            return "Email already registered! Please login."

        connection.close()

        return redirect("/login")

    return render_template("register.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        connection = sqlite3.connect("neurolearn.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        connection.close()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Recommendation Page
@app.route("/recommendation")
def recommendation():
    return render_template("recommendation.html")


if __name__ == "__main__":
    app.run(debug=True)