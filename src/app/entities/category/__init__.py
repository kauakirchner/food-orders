from src.app import DB

class Category(DB.Model):
  __tablename__ = 'categories'
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  name = DB.Column(DB.String(84), nullable=False)
  description = DB.Column(DB.String(84), nullable=False)
  active = DB.Column(DB.Boolean, nullable=False)

  def __init__(self, name: str, description: str, active: bool) -> None:
    self.name = name
    self.description = description
    self.active = active

  @classmethod
  def seed(cls, name: str, description: str, active: bool):
    category = Category(
      name=name,
      description=description,
      active=active
    )
    category.save()

  def save(self):
    DB.session.add(self)
    DB.session.commit()