from flask import Flask
from routes.berry_routes import berry_routes_config
from settings import settings
app = Flask(__name__)
app.config["FLASK_APP"] = settings.flask_app
app.config["FLASK_DEBUG"] = settings.flask_debug
berry_routes_config(app)

if __name__ == '__main__':
    app.run()