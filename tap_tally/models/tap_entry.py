from .. import db


class TapEntry(db.Model):
    __tablename__ = 'tap_entry'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    alc_by_vol = db.Column(db.Float)
    srm = db.Column(db.Integer)
    ibu = db.Column(db.Float)
    description = db.Column(db.String(1000))
    notes = db.Column(db.String(1000))
    visible = db.Column(db.Boolean)
    image = db.Column(db.String(256))
    brewed_on = db.Column(db.DateTime)
    kegged_on = db.Column(db.DateTime)
    keg_no = db.Column(db.Integer)
    tap_number = db.Column(db.Integer)
    consumed = db.Column(db.Boolean)

    def __repr__(self):
        return f'{self.name}'
