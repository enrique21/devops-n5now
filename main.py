from datetime import datetime
from flask import Flask
import pytz
import os

app = Flask(__name__)

def datetime_local():
    dt_local = datetime.now(pytz.timezone('America/Lima'))
    return dt_local.strftime("%Y:%m:%d %H:%M:%S")

@app.route('/')
def hello():
    environment_name = os.environ.get("ENVIRONMENT_NAME")
    return f"<font color='blue'>Hello World (N5 Now)! from <b>{environment_name}</b> (now {datetime_local()})</font>\n"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    #app.run()
