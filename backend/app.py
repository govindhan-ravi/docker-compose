from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend running on port 8080"

if __name__ == "__main__":
    # Must bind 0.0.0.0 to be accessible externally
    app.run(host="0.0.0.0", port=8080)
