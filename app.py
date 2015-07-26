# ----- Flash Hello World ---- #

# import Flask class from flask module
from flask import Flask

# create the applications object
app = Flask(__name__)

app.config["DEBUG"] = True
#use decorators to link the function to a URL

@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string

def hello_world():
    return "Hello, World!??!!!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query
# start the dev server using run()

@app.route("/integer/<int:value>")
def int_type(value):
    print value+1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print value+1
    return "correct"

#dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()
