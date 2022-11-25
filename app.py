"""

RUN THIS FILE TO HOST ON LOCAL HOST WITH DEBUGGER

"""
import os
from flask import Flask, render_template, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # routes to index page
    @app.route("/")
    @app.route("/home")

    def home():
        return render_template("index.html")

    # route to visualizer page
    @app.route("/visualizer")
    def visualizer():
        return render_template("visualizer.html")

    return app

app = create_app()

# hosts files on localhost
if __name__ == "__main__":
    app.run(debug= True, port=5001)
    
