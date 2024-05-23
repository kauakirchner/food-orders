import bcrypt
from src.app import db
from src.app.models.city import City

users_roles = db.Table('users_role',
                    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
                    )


class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  city_id = db.Column(db.Integer, db.ForeignKey(City.id), nullable=False)
  name = db.Column(db.String(84), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  email = db.Column(db.String(84), nullable=False)
  password = db.Column(db.String(84), nullable=False)
  city = db.relationship('City', foreign_keys=[city_id])
  roles = db.relationship('Roles', secondary=[users_roles], backref='users')

  def __init__(self, city_id: int, name: str, age: int, email: str, password: str, roles) -> None:
    self.city_id = city_id
    self.name = name
    self.age = age
    self.email = email
    self.password = password
    self.roles = roles

  def check_password(self, password):
    return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

  @staticmethod
  def encrypt_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

  @classmethod
  def seed(cls, city_id: int, name: str, age: int, email: str, password: str, roles):
    user = User(
      city_id=city_id,
      name=name,
      age=age,
      email=email,
      password=cls.encrypt_password(password.encode("utf-8")),
      roles=roles
    )
    user.save()
  
  def save(self):
    db.session.add(self)
    db.session.commit()
    
  