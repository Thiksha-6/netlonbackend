from app import db
from datetime import datetime

class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "rate": self.rate,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
