from flask import Flask
import time
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status/<int:status>")
def do_status(status):
    return "Status code: {}".format(status), status

@app.route("/sleep/<int:sleep_time>")
def do_sleep(sleep_time):
    time.sleep(sleep_time)
    return "Sleep time: {}".format(sleep_time)

if __name__ == "__main__":
    app.run(debug=True)