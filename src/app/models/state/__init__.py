from src.app import db
from src.app.models.country import Country

class State(db.Model):
  __tablename__ = "states"

  id = db.Column(db.Integer, autoincrement = True, primary_key = True)
  country_id = db.Column(db.Integer, db.ForeignKey(Country.id), nullable = False)
  name = db.Column(db.String(84), nullable = False)
  initials = db.Column(db.String(2), nullable = False)
  country = db.relationship("Country", foreign_keys=[country_id ])

  def __init__(self, country_id, name, initials):
    self.country_id = country_id
    self.name = name
    self.initials = initials

  @classmethod
  def seed(cls, country_id, name, initials):
    state = State(
      country_id=country_id,
      name=name,
      initials=initials
    )
    state.save()
  
  def save(self):
    db.session.add(self)
    db.session.commit()