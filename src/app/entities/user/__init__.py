import bcrypt
from src.app.entities.city import City
from src.app import DB

users_roles = DB.Table('users_role',
                    DB.Column('user_id', DB.Integer, DB.ForeignKey('users.id')),
                    DB.Column('role_id', DB.Integer, DB.ForeignKey('roles.id'))
                    )


class User(DB.Model):
  __tablename__ = 'users'
  id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
  city_id = DB.Column(DB.Integer, DB.ForeignKey(City.id), nullable=False)
  name = DB.Column(DB.String(84), nullable=False)
  age = DB.Column(DB.Integer, nullable=False)
  email = DB.Column(DB.String(84), nullable=False)
  password = DB.Column(DB.String(84), nullable=False)
  city = DB.relationship('City', foreign_keys=[city_id])
  roles = DB.relationship('Roles', secondary=[users_roles], backref='users')

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
    DB.session.add(self)
    DB.session.commit()
    
  