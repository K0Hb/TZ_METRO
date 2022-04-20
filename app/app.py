from flask import Flask, render_template
from forms import Regform

app = Flask(__name__)
app.config['SECRET_KEY'] = '84da5b8a39a6d06bf8bc7a60cedcac93'

@app.route('/', methods = ['POST', 'GET'])
def home():
    form = Regform()
    return render_template('Carousel.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)