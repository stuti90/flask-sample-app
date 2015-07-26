# ----- Flash Hello World ---- #

# import Flask class from flask module
from flask import Flask

# create the applications object
app = Flask(__name__)

#use decorators to link the function to a URL

@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string

def hello_world():
    return "Hello, World!"

# start the dev server using run()

if __name__ == "__main__":
    app.run()
