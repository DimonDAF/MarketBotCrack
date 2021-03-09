import hashlib

from flask import Flask, request

app = Flask(__name__)


@app.route('/OOOOOOOOOOOOOOOOOOOOOOOOOO.php')
def update():
    return {"nupdate": False, "message": ""}


@app.route('/OIhjkgitrjohitkJHIOY4R.php')
def auth():
    to_md5 = "{}-{}-{}".format(request.args.get('OkgotjtorjhoytjOJHYJTYORTGJ'), request.args.get('rtgwipojuhpyktemxczjikfvbiort'), request.args.get('OkgotjtorjhoytjOJHYJTYORTGJ'))
    return {"status": "Authorized", "exp": 999999999999, "token": hashlib.md5(to_md5.encode()).hexdigest(), "message": "Cracked by t.me/lapkidev"}


if __name__ == '__main__':
    app.run(port=80)
