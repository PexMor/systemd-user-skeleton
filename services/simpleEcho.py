#!/usr/bin/env python3

from __future__ import print_function, unicode_literals

from flask import Flask
from flask import Response
from flask import request
from flask import jsonify

HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Eye</title>
  </head>
    <body>
        <h1>Hello World @ HTML</h1>
        <hr />
        <a href='/echo/html/random'>[random echo]</a>
        <hr />
        <a href='/get/ip'>[get remote ip as json]</a>
    </body>
</html>"""


def serve():
    global app
    app = Flask(__name__)

    @app.route("/")
    def basePage():
        return Response(HTML, mimetype='text/html')

    @app.route("/echo/html/<txt>")
    def echo_html(txt):
        return Response(f"<html><body>u sent {txt}</body></html>", mimetype='text/html')

    @app.route("/get/ip")
    def get_ip():
        return jsonify({'ip': request.remote_addr}), 200


if __name__ == "__main__":
    print("Application started directly")
elif __name__ == "simpleEcho":
    serve()
else:
    print("__name__: " + __name__)
