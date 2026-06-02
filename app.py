from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hallo Azure!</h1>
    <p>Diese Webseite wurde über GitHub deployed.</p>
    """

if __name__ == "__main__":
    app.run()
