from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<senderID>")
def redirect_code(senderID):
    return render_template("receive.html", senderID=senderID)


if __name__ == "__main__":
    app.run()