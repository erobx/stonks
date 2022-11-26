"""

RUN THIS FILE TO HOST ON LOCAL HOST WITH DEBUGGER

"""
import os
from flask import Flask, render_template, request

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "stonks.sqlite")
    )

    # routes to index page
    @app.route("/")
    def index():
        return render_template("index.html")

    # route to visualizer page
    @app.route("/visualizer")
    def visualizer():
        return render_template("visualizer.html")

    #from stonks import db
    #db.init_app(app)

    return app

