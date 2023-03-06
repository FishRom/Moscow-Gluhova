from flask import Flask, render_template

app = Flask(__name__)

# /results/Mark/3/68.2
#@app.route('/<title_name>')
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def index(nickname, level, rating):
    return render_template('base_1.html', name=nickname, lvl=level, rat=rating)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')