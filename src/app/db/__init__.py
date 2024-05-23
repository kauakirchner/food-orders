import requests
from src.app.models.city import City
from src.app.models.state import State
from src.app.models.country import Country
from src.app.models.user import User
from src.app.models.city.schema import cities_share_schema
from src.app.models.state.schema import states_share_schema
from src.app.models.country.schema import country_share_schema
from src.app import db

def populate_db():
  country = Country.query.first()
  if country is not None:
      print('Já existe dados populados')
      return
  
  brasil_code = 76

  try:
    countries_data = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/paises/{brasil_code}')
    states_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
    cities_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/municipios")

    country_name = countries_data.json()[0]['nome']
    Country.seed(country_name, 'Português')
    db.session.commit()  # Commit the country to the database
    country = Country.query.filter_by(name=country_name).first()
    country_dict = country_share_schema.dump(country)
    
    for stateObject in states_data.json():
      State.seed(
        country_dict['id'],
        stateObject['nome'],
        stateObject['sigla']
      )
    db.session.commit()  # Commit the states to the database
    
    state = State.query.order_by(State.name.asc()).all()
    state_dict = states_share_schema.dump(state)

    for city_object in cities_data.json():
      state_id = next((state_obj['id'] for state_obj in state_dict if state_obj['initials'] == city_object['microrregiao']['mesorregiao']['UF']['sigla']), None)
      if state_id:
        City.seed(
          state_id,
          city_object['nome']
        )
    db.session.commit()  # Commit the cities to the database

    cities = City.query.order_by(City.name.asc()).all()
    cities_dict = cities_share_schema.dump(cities)
    users = requests.get('https://randomuser.me/api?nat=br&results=100')
    
    for user in users.json()['results']:
      city_id = next((city_obj['id'] for city_obj in cities_dict if user['location']['city'] == city_obj['name']), 2)
      User.seed(
        city_id,
        user['name']['first'] + ' ' + user['name']['last'],
        user['registered']['age'],
        user['email'],
        user['login']['password']
      )
    db.session.commit()  # Commit the users to the database
    users = User.query.order_by(User.name.asc()).all()
    print("Dados inseridos com sucesso.")
  
  except Exception as e:
    print(f"Error populating the database: {e}")
    db.session.rollback()
  return

def delete_tables():
  db.drop_all()