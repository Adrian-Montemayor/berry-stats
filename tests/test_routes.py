from flask import Flask
from routes.berry_routes import berry_routes_config
from settings import settings
def test_index():
    app = Flask(__name__)
    app.config["FLASK_APP"] = settings.flask_app
    app.config["FLASK_DEBUG"] = settings.flask_debug
    berry_routes_config(app)
    client = app.test_client()
    r = client.get('/')

    assert r.status_code == 200
    assert r.json["hi"] == "hello"