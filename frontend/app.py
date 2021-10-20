from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('landing_page.html', page_name="Automation Home")

@app.route("/admin")
def admin():
    return render_template('landing_page.html', page_name="Automation Admin")
