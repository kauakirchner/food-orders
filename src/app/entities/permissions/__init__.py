from src.app import DB

class Permission(DB.Model):
  __tablename__ = 'permissions'
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  description = DB.Column(DB.String(84), nullable=False)

  def __init__(self, description: str) -> None:
    self.description = description

  @classmethod
  def seed(cls, description):
    permission = Permission(
      description=description
    )
    permission.save()

  def save(self):
    DB.session.add(self)
    DB.session.commit()
