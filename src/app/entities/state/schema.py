from src.app import MA
from src.app.entities.country.schema import country_share_schema

class StateSchema(MA.Schema):
  country = MA.Nested(country_share_schema)
  class Meta:
    fields = ('id', 'country_id', 'country', 'name', 'initials')

state_share_schema = StateSchema()
states_share_schema = StateSchema(many=True)