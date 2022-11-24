"""

RUN THIS FILE TO HOST ON LOCAL HOST WITH DEBUGGER

"""
from flask import Flask, render_template, request

app = Flask(__name__)

# routes to index page

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html")

# route to visualizer page

@app.route("/visualizer")
def visualizer():
    return render_template("visualizer.html")

# hosts files on localhost

if __name__ == "__main__":
    app.run(debug= True, port=5001)
    
