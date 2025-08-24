from flask import Flask, redirect, abort, Response
import json

app = Flask(__name__)

def load_shortcuts():
    with open('shortcuts.json') as f:
        return json.load(f)

def load_work_shortcuts():
    with open('work_shortcuts.json') as f:
        return json.load(f)

def load_personal_shortcuts():
    with open('personal_shortcuts.json') as f:
        return json.load(f)

@app.route("/<path>")
def go(path):
    shortcuts = load_shortcuts()
    work_shortcuts = load_work_shortcuts()
    personal_shortcuts = load_personal_shortcuts()

    url = shortcuts.get(path) or work_shortcuts.get(path) or personal_shortcuts.get(path)
    if url:
        return redirect(url)
    return custom_404(None)


@app.route("/")
def index():
    return load_shortcuts()


@app.errorhandler(404)
def custom_404(e):
    shortcuts = load_shortcuts()
    links = "".join(
        f'<li><a href="/{key}">{key}</a> → {value}</li>'
        for key, value in shortcuts.items()
    )
    html = f"""
    <html>
        <head><title>Shortcut Not Found</title></head>
        <body style="font-family: sans-serif;">
            <h1>404 – Shortcut Not Found</h1>
            <p>Here are the available shortcuts:</p>
            <ul>{links}</ul>
        </body>
    </html>
    """
    return Response(html, status=404, mimetype='text/html')

app.run(host="0.0.0.0", port=8080)