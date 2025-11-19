favorite_places = {'elkin': {'Miami',
                           'Orlando',
                           'Las Olas'},
                    'Nelson': {'Miami',
                               'Fort Lauderdale',
                               'New york'},
                    'Nelson Sr.': {'Choluteca',
                                   'Valle de angeles',
                                   'los sauces'}
                    }
for name, places in favorite_places.items():
    print(f"\n{name} favorite places:")
    for place_name in places:
        print(place_name)