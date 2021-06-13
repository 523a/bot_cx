from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def post_bot_response():
    userText = request.args.get('msg')
    return (dp(userText))

def dp(ph):
    text={'id':'ч','sent': 0,'text':ph,'time':''}
    r = requests.post('http://172.16.0.145:5100/bot', json=text).json()
    return (r[-1]['text'])


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5200)#(host = '0.0.0.0', port=5100)
