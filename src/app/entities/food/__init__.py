from src.app import DB
from src.app.entities.category import Category

class Food(DB.Model):
  __tablename__ = 'food'
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  category_id = DB.Column(DB.Integer, DB.ForeignKey(Category.id), nullable=False)
  active = DB.Column(DB.Boolean, nullable=False)
  price = DB.Column(DB.Float, nullable=False)
  units = DB.Column(DB.Integer, nullable=False)
  available = DB.Column(DB.Boolean, nullable=False)
  name = DB.Column(DB.String(84), nullable=False)
  description = DB.Column(DB.String(84), nullable=False)
  images = DB.Column(DB.ARRAY(DB.String(84)), nullable=False)
  category = DB.relationship("Category", foreign_keys=[category_id])

  def __init__(self, active, price, units, available, name, description, category_id) -> None:
    self.active = active
    self.price = price
    self.units = units
    self.available = available
    self.name = name
    self.description = description
    self.category_id = category_id

  @classmethod
  def seed(cls, active, price, units, available, name, description, category_id, images):
    role = Food(
      active=active,
      price=price,
      units=units,
      available=available,
      name=name,
      category_id=category_id,
      description=description,
      images=images
    )
    role.save()

  def save(self):
    DB.session.add(self)
    DB.session.commit()