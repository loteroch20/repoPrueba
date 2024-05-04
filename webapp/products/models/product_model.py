from users.models.db import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    typee = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(30), nullable=False)
    due_date = db.Column(db.String(100), nullable=False)

    def __init__(self, name, typee, price, due_date):
        self.name = name
        self.typee = typee
        self.price = price
        self.due_date = due_date
