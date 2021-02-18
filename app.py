import os
from flask import Flask
app = Flask(__name__)
import yaml
with open('/config/config.yml') as data:
     config=yaml.safe_load(data)


@app.route("/")
def main():
    return ("Welcome to "+ config['env'] +" !")

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9898)
