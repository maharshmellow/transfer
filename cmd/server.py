from flask import Flask, jsonify, render_template, request, redirect
import validators
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import socket
import ngrok

app = Flask(__name__)

# called when a file is being received
@app.route("/receive", methods=["POST"])
def receive():
    if request.method == "POST":
        if "file" in request.files:
            file = request.files['file']
            file.save(file.filename)
            return "File Transfer Completed" 
        else:
            return "File not provided"
    return "Invalid"

@app.route("/")
def index():
    return "working" 

def startServer():
    try:
        print(ngrok.client.get_tunnels()[0].public_url)
    except:
        return 

    app.run()


# https://gist.github.com/betrcode/0248f0fda894013382d7
def isOpen(ip, port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

startServer()

# print(isOpen("127.0.0.1", 5000))

# if __name__ == "__main__":
#     app.run()


