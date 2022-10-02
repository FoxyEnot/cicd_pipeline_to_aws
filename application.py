
from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello World from Flask page"

@application.route("/help")
def help():
    return "This is a help page"

@application.route("/users")
def userpage():
    return "This is a users page"

@application.route("/users/<username>")
def user(username):
    return "This is " + username.upper()

@application.route("/path/<path:subp>")
def subpath(subp):
    return "This is " + subp.upper()

@application.route("/htmlpage")
def showhtmlpage():
    myfile = open("mypage.html", mode="r")
    page = myfile.read()
    myfile.close()
    return page


if __name__ == "__main__":
   # application.debug = True
   # application.env = "FirstFlask"
    application.run()



