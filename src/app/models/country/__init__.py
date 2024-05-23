from src.app import db

class Country(db.Model):
  __tablename__ = 'countries'
  id = db.Column(db.Integer, autoincrement = True, primary_key = True)
  name = db.Column(db.String(84), nullable = False)
  language = db.Column(db.String(84), nullable = False)

  def __init__(self, name: str, language: str) -> None:
    self.name = name
    self.language = language

  @classmethod
  def seed(cls, name, language):
    country = Country(
      name=name,
      language=language
    )
    country.save()

  def save(self):
    db.session.add(self)
    db.session.commit()
  

