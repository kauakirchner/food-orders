from src.app import db

class Permission(db.Model):
  __tablename__ = 'permissions'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  description = db.Column(db.String(84), nullable=False)

  def __init__(self, description: str) -> None:
    self.description = description

  @classmethod
  def seed(cls, description):
    permission = Permission(
      description=description
    )
    permission.save()

  def save(self):
    db.session.add(self)
    db.session.commit()
