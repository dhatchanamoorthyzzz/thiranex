

from flask import Flask, render_template_string, request, redirect, url_for, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Use environment variable in production
bcrypt = Bcrypt(app)

# Dummy user database (replace with real DB)
users = {
    "admin": bcrypt.generate_password_hash("Admin@123").decode("utf-8")
}

# HTML templates
login_page = """
<!DOCTYPE html>
<html>
<head><title>Secure Login</title></head>
<body>
    <h2>Login</h2>
    <form method="POST">
        Username: <input type="text" name="username" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
    <p>{{ message }}</p>
</body>
</html>
"""

dashboard_page = """
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
    <h2>Welcome, {{ user }}!</h2>
    <p>You have successfully logged in.</p>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and bcrypt.check_password_hash(users[username], password):
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            message = "Invalid credentials. Please try again."
    return render_template_string(login_page, message=message)

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template_string(dashboard_page, user=session["user"])
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
