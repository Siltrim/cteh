from flask_wtf import FlaskForm
from wtforms import StringField, validators


class QrCodeForm(FlaskForm):
    text_to_qrcode = StringField(label='text 2 qrcode', validators=[validators.length(min=5, max=140),])