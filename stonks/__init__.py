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
        network = Network(height="100vh", neighborhood_highlight=True)
        network.toggle_physics(True)
        if request.method == "POST":
            ticker = request.form['ticker']
            sort = request.form['optradio']
            src = net.init_network(db_path, net=network, id=ticker, sort=sort, depth=10, k=10)
            if (src is not None ):
                bfs, bfsTime = net.bfs(ticker, network)
                dfs, dfsTime = net.bfs(ticker, network)
                bfsTime = str((bfsTime * 1000))[:6] + "ms"
                dfsTime = str((dfsTime * 1000))[:6] + "ms"
                sector = src.sector
                price = "$"+ str(src.price)
                pe = src.pe
                volume = "{:,}".format(src.volume)
                employees = "{:,}".format(src.employees)
                eps = src.eps
                revenue = "${:,}".format(src.revenue)
                growth = src.growth
                profit = "${:,}".format(src.profit)
                return render_template("visualizer.html", ticker=ticker, sector=sector, price=price, pe=pe, volume=volume, employees = employees, 
                                    eps=eps, revenue=revenue, growth=growth, profit=profit, bfs=bfs, bfsTime = bfsTime, dfs=dfs, dfsTime = dfsTime)
            
        return render_template("visualizer.html")


    return app

