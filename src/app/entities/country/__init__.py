from src.app import DB

class Country(DB.Model):
  __tablename__ = 'countries'
  id = DB.Column(DB.Integer, autoincrement = True, primary_key = True)
  name = DB.Column(DB.String(84), nullable = False)
  language = DB.Column(DB.String(84), nullable = False)

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
    DB.session.add(self)
    DB.session.commit()
  

