from src.app import db

role_permissions = db.Table('role_permissions',
                    db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
                    db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id'))
)

class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  description = db.Column(db.String(84), nullable=False)
  permissions = db.relationship('Permission', secondary=role_permissions, backref='roles')

  def __init__(self, description: str, permissions) -> None:
    self.description = description
    self.permissions = permissions

  @classmethod
  def seed(cls, description, permissions):
    role = Role(
      description=description,
      permissions=permissions
    )
    role.save()

  def save(self):
    db.session.add(self)
    db.session.commit()