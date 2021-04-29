from flask import Flask, render_template, request, url_for
app = Flask(__name__)


#@app.route('/', methods=['GET'])
#def hello():
#	return "Hello! Welcome to my page :)."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    return render_template('check.html')

@app.route('/dropdown', methods=['GET'])
def dropdown():
    colours = ['Red', 'Blue', 'Green']#'Black', 'Orange', 'Green', 'Magenta', 'Yellow']
    return render_template('test.html', colours=colours)

@app.route('/toggle', methods=['GET'])
def toggle():
    colours = ['Red', 'Blue', 'Green']#'Black', 'Orange', 'Green', 'Magenta', 'Yellow']
    return render_template('toggle.html', colours=colours)

if __name__ == "__main__":
    app.run(debug=True)
