from src.app import ma
from src.app.models.country.schema import country_share_schema

class StateSchema(ma.Schema):
  country = ma.Nested(country_share_schema)
  class Meta:
    fields = ('id', 'country_id', 'country', 'name', 'initials')

state_share_schema = StateSchema()
states_share_schema = StateSchema(many=True)