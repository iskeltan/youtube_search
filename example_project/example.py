# -*- coding: utf-8 -*-
import json
from flask import Flask, request
from youtube.youtube import Youtube
app = Flask(__name__)

@app.route('/', methods=['GET', ])
def hello():
    q = request.args.get('q', False)
    html = """<form method="GET" action="/">
                <input type="text" placeHolder="search" name="q">
                <input type="submit" value="search">
              </form>
           """
    if not q:
        return html

    youtube = Youtube()
    results = youtube.search(q)
    return json.dumps(results)

if __name__ == "__main__":
    app.run()
