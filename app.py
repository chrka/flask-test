from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("template.xhtml")

@app.route('/endpoint', methods=['GET', 'POST'])
def endpoint():
    method = 'POST' if request.method == 'POST' else 'GET'
    return render_template("endpoint.xhtml", method=method)


if __name__ == '__main__':
    app.run()
