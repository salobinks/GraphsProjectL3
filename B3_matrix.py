import os
from tabulate import tabulate
from colorama import Fore


# Lit le contenu du fichier spécifié par le numéro de la table
def read_data(number):
    # Lit le contenu du fichier spécifié par le numéro du tableau de contraintes
    file_path = f'data/table {number}.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        return None


# Lit + enregistre les données de la table de contraintes sous forme de matrice
def matrice_table(number):
    table = []
    data_table = read_data(number)

    if data_table is None:
        print(f"Le fichier pour le tableau de contraintes numéro {number} est introuvable.")
        return []

    # Traitez les données de la table
    lines = data_table.strip().split('\n')
    for line in lines:
        columns = line.strip().split()
        current_state = int(columns[0])
        transition_time = int(columns[1])
        previous = [int(x) for x in columns[2:]] if len(columns) > 2 else [0]
        table.append((current_state, transition_time, previous))

    return table


# Afficher la matrice des valeurs
def display_value_matrix(graph_data):
    # Identifier tous les sommets (états) présents
    all_states = set(graph_data.keys())
    # Déterminer la taille de la matrice
    num_states = max(all_states) + 1  # Assure qu'alpha (0) et omega (N+1) sont inclus

    # Initialiser la matrice avec des valeurs '*' partout
    matrix = [['*' for _ in range(num_states)] for _ in range(num_states)]

    # Remplir la matrice avec les durées appropriées
    for state, data in graph_data.items():
        for successor in data['successors']:
            duration_str = str(data['duration'])
            # Colorier la durée si ce n'est pas un '*'
            color_duration = Fore.LIGHTGREEN_EX + duration_str + Fore.RESET if duration_str != '*' else '*'
            matrix[state][successor] = color_duration

    # Afficher la matrice
    headers = [''] + [str(i) for i in range(num_states)]
    rows = [[str(i)] + row for i, row in enumerate(matrix)]
    print(tabulate(rows, headers=headers, tablefmt='presto', numalign='center', stralign='center'))