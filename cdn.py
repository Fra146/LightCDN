#!/usr/bin/python3
import json, os, yaml, time, sys
from flask import Flask, render_template
from flask_autoindex import AutoIndex

start_time = time.time()

with open("settings.yml", "r") as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)


app = Flask(__name__)

AutoIndex(app,browse_root=settings['files_path'])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', 404)

if settings['status_path'] != "OFF":
    @app.route(settings['status_path'])
    def status():
        return render_template("status.html", version=settings['version'], uptime=time.time()-start_time)


if __name__ == "__main__":
    app.run()