from src.app import db
from src.app.models.categories import Categorie

class Food(db.Model):
  __tablename__ = 'food'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  active = db.Column(db.Boolean, nullable=False)
  price = db.Column(db.Float, nullable=False)
  units = db.Column(db.Integer, nullable=False)
  available = db.Column(db.Boolean, nullable=False)
  name = db.Column(db.String(84), nullable=False)
  description = db.Column(db.String(84), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey(Categorie.id), nullable=False)

  def __init__(self, active, price, units, available, name, description, category_id) -> None:
    self.active = active
    self.price = price
    self.units = units
    self.available = available
    self.name = name
    self.description = description
    self.category_id = category_id

  @classmethod
  def seed(cls, active, price, units, available, name, description, category_id):
    role = Food(
      active=active,
      price=price,
      units=units,
      available=available,
      name=name,
      category_id=category_id,
      description=description,
    )
    role.save()

  def save(self):
    db.session.add(self)
    db.session.commit()