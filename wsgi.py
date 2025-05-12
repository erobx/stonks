'''
Run to create the app

Need MANIFEST.in for includes and config
Still need to work on configuration files
'''

from stonks_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5001)