'''
Run to create the app

Need MANIFEST.in for includes and config
Still need to work on configuration files
'''

from stonks import create_app
import subprocess

app = create_app()

if __name__ == "__main__":
    #subprocess.run(["flask", "--app", "stonks", "init-db"])
    app.run(debug=True, port=5001)