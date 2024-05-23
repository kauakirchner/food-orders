from src.app import DB
from src.app.models.categories import Categorie

class Food(DB.Model):
  __tablename__ = 'food'
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  active = DB.Column(DB.Boolean, nullable=False)
  price = DB.Column(DB.Float, nullable=False)
  units = DB.Column(DB.Integer, nullable=False)
  available = DB.Column(DB.Boolean, nullable=False)
  name = DB.Column(DB.String(84), nullable=False)
  description = DB.Column(DB.String(84), nullable=False)
  category_id = DB.Column(DB.Integer, DB.ForeignKey(Categorie.id), nullable=False)

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
    DB.session.add(self)
    DB.session.commit()