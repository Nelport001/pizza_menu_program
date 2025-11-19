cities = {'Miami': {'country': 'United States',
                    'population': '442,241',
                    'fact': 'Miami is the only major U.S. city founded by a woman'},
            'Madrid': {'country': 'Spain',
                       'population': '3,400,000',
                       'fact': 'home to the worlds oldest continuously operating restaurant'},
            'Tegucigalpa': {'country': 'Honduras',
                            'population': '3,000,000',
                            'fact': 'One of the presidents was sent to prison for Narcotrafic'}}
question = input("Choose a city (Miami, Madrid, Tegucigalpa):")
if question == 'Miami':
    miami = f"{cities['Miami']}"
    print(miami)




# for city, info in cities.items():
#     print(f"\n{city}:")
#     country = f"Country:{info['country']}"
#     population = f"Population:{info['population']}"
#     fact = f"Fact:{info['fact']}"
#     print(country)
#     print(population)
#     print(fact)
    