from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form')
def test():
    return render_template("index.html")

@app.route('/') 
def mapPage():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug = True)
#to do: make chatbot