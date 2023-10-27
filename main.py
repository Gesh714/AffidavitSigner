from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__,template_folder= 'templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class AffidavitSigner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    signature = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<AffidavitSigner {self.name}>'

def create_tables():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()