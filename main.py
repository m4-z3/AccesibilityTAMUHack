from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

@app.route('/')
def test():
    return render_template("index.html")

@app.route('/map') 
def mapPage():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug = True)