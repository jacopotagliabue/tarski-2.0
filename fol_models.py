FOL_TEST_WORLD = {
    'domain': [1, 2, 3, 4],
    'constants': {
        'a': 1,
        'b': 2,
        'c': 3
    },
    'extensions': {
        "P": [[1]],
        "R": [[1], [2], [4]],
        "Q": [[1], [2], [3], [4]],
        "C": [[1, 2], [2, 3]],
        "D": [[2, 3]]
    }
}

# see readme for link to original blog post
FOL_MEDIUM_WORLD = {
    'domain': [1, 2, 3, 4, 5],
    'constants': {
        'j': 1,  # 'Jacopo'
        'm': 2,  # 'Mattia'
        'r': 3,  # 'Ryan'
        'c': 4,  # 'Ciro'
    },
    'extensions': {
        "I": [[1], [2], [4]],  # 'IsItalian'
        "P": [[5]],  # 'IsAmerican'
        "Q": [[3]]  # 'IsCanadian'
    }
}