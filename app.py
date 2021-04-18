import requests, json
from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__) #create new instance of flask
@app.route("/")
def root():
    return render_template("index.html")

@app.route("/buy")
def buy():
    return render_template("buy.html")

@app.route("/redeem")
def redeem():
    return render_template("redeem.html")

@app.route("/check")
def check():
    creds = get_creds(request.args.get('code'))
    if creds == 0:
        return redirect("/redeem")
    return render_template("redeem.html", creds = creds)

def get_creds(code):
    acc_type = code.split("-")[0].lower()
    if acc_type not in ["crunchy", "disney"] :
        return 0
    url = "https://automated.pw/api/{acc}/redeem?key={code}".format(acc=acc_type, code = code)
    request = requests.get(url)
    data = json.loads(request.text)
    return data["message"]["account"]

if __name__ == "__main__":
    app.debug = True
    app.run()