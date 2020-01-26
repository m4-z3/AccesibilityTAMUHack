from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english

@app.route('/')
def test():
    return render_template("index.html")

<<<<<<< HEAD
@app.route('/map') 
def mapPage():
    return render_template("map.html")
=======
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
<<<<<<< HEAD
    return str(englishBot.get_response(userText))

=======
    return str(englishBot.get_response(userText)
>>>>>>> 5b29e16ba5a4c1165331ed066d77d2d13518259c
>>>>>>> ad6f3970cc20c3d846e16b906fb9f029035f4c50

if __name__ == "__main__":
    app.run(debug = True)