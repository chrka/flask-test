from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    method = 'POST' if request.method == 'POST' else 'GET'
    return render_template("template.xhtml", method=method)


if __name__ == '__main__':
    app.run()
