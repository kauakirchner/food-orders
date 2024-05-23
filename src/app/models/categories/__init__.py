from src.app import db

class Categorie(db.Model):
  __tablename__ = 'categories'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  name = db.Column(db.String(84), nullable=False)
  description = db.Column(db.String(84), nullable=False)
  active = db.Column(db.Boolean, nullable=False)

  def __init__(self, name: str, description: str, active: bool) -> None:
    self.name = name
    self.description = description
    self.active = active

  @classmethod
  def seed(cls, name: str, description: str, active: bool):
    role = Categorie(
      name=name,
      description=description,
      active=active
    )
    role.save()

  def save(self):
    db.session.add(self)
    db.session.commit()