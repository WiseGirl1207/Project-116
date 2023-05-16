from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():

    name = "Ahaana" 
    age = "13" 

    return render_template('index.html' , name = name , age = age)

@app.route("/dad")
def homeDad():

    name = "Vivek" 
    age = "44" 

    return render_template('index.html' , name = name , age = age)

@app.route("/mom")
def homeMom():

    name = "Poornima" 
    age = "44" 

    return render_template('index.html' , name = name , age = age)

@app.route("/friend")
def homeFriend():

    name = "Anoushka" 
    age = "14" 

    return render_template('index.html' , name = name , age = age)

if __name__  ==  '__main__':
    app.run(debug=True)
