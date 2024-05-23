
from src.app import MA
from src.app.models.state.schema import state_share_schema

class CitySchema(MA.Schema):
  state = MA.Nested(state_share_schema)
  class Meta:
    fields = ('id', 'state_id', 'state' 'name')

city_share_schema = CitySchema()
cities_share_schema = CitySchema(many=True)