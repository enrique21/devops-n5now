from datetime import datetime
import pytz
from flask import Flask

app = Flask(__name__)

def datetime_local():
    dt_local = datetime.now(pytz.timezone('America/Lima'))
    return dt_local.strftime("%Y:%m:%d %H:%M:%S")

@app.route('/')
def hello():
    return "Hello World (N5 Now)! (now %s)\n" % datetime_local()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    #app.run()
