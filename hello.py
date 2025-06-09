from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    #return "<p>Hello, World!</p>"
    message = os.getenv("CUSTOM_MESSAGE", "Hello, World!")
    return f"<p>{message}</p>"
