from flask import Flask, request

app = Flask(__name__)


@app.route('/sum2/', methods=['POST'])
def sum2():
    print(request.json)
    a = request.json['data']
    return {'sum': sum(a)}

@app.route('/sum/', methods=['POST'])
def sum1():
    print(request.json)
    a = request.json['a']
    b = request.json['b']
    return {'sum': a + b}

app.run()