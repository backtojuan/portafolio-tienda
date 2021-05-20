from flask import Flask, render_template, abort
from model import ARIMA

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

##app.add_url_rule('/',view_func=ARIMA.predecir);



if __name__ == "__main__":
    app.run(debug=True)