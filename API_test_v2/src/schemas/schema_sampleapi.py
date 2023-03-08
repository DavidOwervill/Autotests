CHARACTER_SCHEMA = {
    "type": "object",
    "properties": {
        'id': {"type": "number"},
        "name": {"type": "string"},
        'status': {'type': "string"},
        'species':{"type": 'string'},
        'type': {'type': 'string'},
        'gender': {'type': 'string'},
        'origin': {'type': 'string'},
        'image': {'type': 'string'}
    },
    "required": ['id']
}


# [{'id': 1, 'name': 'Rick Sanchez', 'status': 'Alive', 'species': 'Human',
# 'type': 'Human', 'gender': 'Male', 'origin': 'Earth (C-137)',
# 'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'}