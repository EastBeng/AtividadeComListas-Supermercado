from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "http://6b0b-35-185-107-52.ngrok.io/"

@app.route('/')
def hello_world():  # put application's code here
    requisicao = requests.get(url)
    JSON = requisicao.json()
    return render_template("index.html", lista=JSON)


if __name__ == '__main__':
    app.run()
