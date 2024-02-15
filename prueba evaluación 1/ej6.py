def separar_personajes(personajes):
    humanos = []
    no_humanos = []
    
    for personaje in personajes:
        if personaje['es_humano']:
            humanos.append(personaje['nombre'])
        else:
            no_humanos.append(personaje['nombre'])
    
    return sorted(humanos), sorted(no_humanos)

personajes = [
    {'nombre': 'Mario', 'es_humano': True},
    {'nombre': 'Luigi', 'es_humano': True},
    {'nombre': 'Donkey Kong', 'es_humano': False},
    {'nombre': 'Peach', 'es_humano': True},
    {'nombre': 'Yoshi', 'es_humano': False},
    {'nombre': 'Bowser', 'es_humano': False},
    {'nombre': 'Toad', 'es_humano': False},
    {'nombre': 'Wario', 'es_humano': True},
]

humanos, no_humanos = separar_personajes(personajes)
print('Humanos:', humanos)
print('No humanos:', no_humanos)


