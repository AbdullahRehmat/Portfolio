# Import Modules Here:
import os

# Import Flask Framework Here:
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
app = Flask(__name__)

# ./Home Script:
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

# ./404 Page:
@app.errorhandler(404)
def page_not_found(e):
    # 404 status set explicitly
    return render_template('404.html'), 404


# Flask Debug Script:s
if __name__ == "__main__":
    app.run(debug="true")