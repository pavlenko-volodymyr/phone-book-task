from town_phone_book import db


class Directory(db.Model):
    __tablename__ = 'directory'

    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(), nullable=True)
    first_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=True)
    phone_number = db.Column(db.String(), nullable=True)
    address = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f'<Directory {self.id}>'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'district': self.district,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
            'address': self.address,
        }
