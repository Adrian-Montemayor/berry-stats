from flask import jsonify, redirect, url_for, render_template
from repositories.api_calls import ApiCalls
from settings import settings

berry_list = []
def berry_routes_config(app):
    @app.route('/')
    def index():
        return jsonify({"hi": "hello"})

    @app.route('/allBerryStats')
    def berry_stats():
        global berry_list
        if not berry_list:
            berry_list = ApiCalls.get_berries(settings.base_url)
            return jsonify(berry_list)
        else:
            return jsonify(berry_list)

    @app.route('/allBerryStats/histogram')
    def histogram():
        global berry_list
        if not berry_list:
            return render_template('histogram.html')
        else:
            return render_template("histogram.html", histo="histo.png")

    @app.errorhandler(404)
    def page_not_found(error):
        return redirect(url_for('index'))