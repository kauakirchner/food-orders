from src.app.models.state import State
from src.app import db

class City(db.Model):
  __tablename__ = 'cities'

  id = db.Column(db.Integer, autoincrement = True, primary_key = True)
  state_id = db.Column(db.Integer, db.ForeignKey(State.id), nullable = False)
  name = db.Column(db.String(84), nullable = False)
  state = db.relationship('State', foreign_keys=[state_id])

  def __init__(self, state_id, name):
    self.state_id = state_id
    self.name = name

  @classmethod
  def seed(cls, state_id, name):
    city = City(
      state_id=state_id,
      name=name
    )
    city.save()
  
  def save(self):
    db.session.add(self)
    db.session.commit()