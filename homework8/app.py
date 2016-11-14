from flask import Flask, request, render_template, send_file
from forms import QrCodeForm
from models import QrCodeModel

import config
import pyqrcode

app = Flask('__name__', template_folder='templates')
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def home():
    qr_file = None
    if request.method == 'POST':
        form = QrCodeForm(request.form)
        if form.validate():
            model = QrCodeModel(form.data)
            qrtext = pyqrcode.create(model.text)
            qr_file = 'qr_file.svg'

            qrtext.svg(qr_file, scale=8)
        else:
            pass
    else:
        form = QrCodeForm()
    return render_template('home.html', form=form, items=qr_file, )


@app.route('/qr_file.svg')
def send_qr_code():
    return send_file('qr_file.svg')

if __name__ == '__main__':
    app.run()
