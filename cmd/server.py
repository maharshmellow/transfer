from flask import Flask, jsonify, render_template, request, redirect
import validators
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
import socket

app = Flask(__name__)

# called when a file is being received
@app.route("/receive", methods=["POST"])
def receive():
    if request.method == "POST":
        message = request.values.get("message")

def startServer():
    app.run()

    if isOpen("127.0.0.1", 5000):
        print("Do Something")

    else:
        print("Please open port 5000 to continue")


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


