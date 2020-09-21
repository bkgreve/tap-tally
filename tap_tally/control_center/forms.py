import datetime as datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, \
    DateField, DecimalField, TextAreaField, BooleanField, \
    SelectField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Optional


class TapEntryForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.brewed_on.data:
            self.brewed_on.data = datetime.datetime.today()

    name = StringField('Beer Name',
                       validators=[DataRequired()]
                       )
    tap_number = IntegerField('Tap Number',
                              validators=[Optional()]
                              )
    alc_by_vol = DecimalField('ABV',
                              places=1,
                              validators=[Optional()]
                              )
    srm = IntegerField('SRM',
                       validators=[Optional()]
                       )
    ibu = DecimalField('IBU',
                       validators=[Optional()]
                       )
    keg_no = IntegerField('Keg Number',
                          validators=[Optional()]
                          )
    description = TextAreaField('Beer Description',
                                validators=[Optional()]
                                )
    visible = BooleanField('Show beer in tap list?',
                           validators=[Optional()]
                           )
    image = FileField('Upload image',
                      validators=[Optional()]
                      )
    notes = TextAreaField('Notes',
                          validators=[Optional()]
                          )
    brewed_on = DateField("Brewed on Date",
                          format="%m/%d/%Y",
                          validators=[DataRequired()],
                          )
    kegged_on = DateField("Kegged on Date",
                          format="%m/%d/%Y",
                          validators=[Optional()]
                          )
    submit = SubmitField('Add Entry')


class SelectEntries(FlaskForm):
    visible_entries = SelectField()
    submit = SubmitField('View/Edit Entry')
