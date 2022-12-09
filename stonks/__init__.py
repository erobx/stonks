"""

RUN THIS FILE TO HOST ON LOCAL HOST WITH DEBUGGER

"""
import os
from flask import Flask, render_template, request
from pyvis.network import Network

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "stonks.db")
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # routes to index page
    @app.route("/")
    def index():
        return render_template("index.html")

    db_path = os.path.abspath('stonks/stonks.db')
    
    from . import net
    
    # route to visualizer page
    @app.route("/visualizer", methods=["GET", "POST"])
    def visualizer():
        if request.method == "POST":
            ticker = request.form['ticker']
            sort = request.form['optradio']
            network = Network(height="100vh", neighborhood_highlight=True)
            network.toggle_physics(True)
            net.init_network(db_path, net=network, id=ticker, sort=sort, depth=10, k=10)
            
        return render_template("visualizer.html")


    return app

