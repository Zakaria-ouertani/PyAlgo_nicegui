from nicegui import ui
from cours import intro


def show():
    expansion_contents = [
            ["Introduction", intro.show],
            ["Les Tableaux", intro.show],
            ["Les Sous-programmes",intro.show],
            ["Les Méthodes de tris et de recherche", intro.show],
            ["Les Enregistrements", intro.show],
            ["Les Fichiers",intro.show],
            ["La Recursivité", intro.show],
            ["La Récurrence", intro.show],
            ["L'Approximation", intro.show]
        ]

    trees = expansion_trees()
    expansions_number = len(expansion_contents)
    expansion_width = 100 / expansions_number
    for i in range(0, expansions_number):
        with ui.column().style(
            "width:100%; border:solid black 1px; margin-top:3px;"
        ):
            with ui.expansion(f"{i + 1}. {expansion_contents[i][0]}", icon="book").classes("w-full h-full").style(
                    "font-size:20px; height:100%; padding:5px;"
            ):
                ui.tree(trees[0], label_key="id", on_select=lambda: ui.open("/Introduction")).props("no-transition accordion")


def expansion_trees():
    intro = [
        {
        "id": "L'algorithme",
        "children": 
            [
                {"id": "La Forme Générale 'un Algorithme"},
                {"id": "Les Syntaxes et Structures Slgorithmiques."}
            ]
        }
    ]
    return [intro]
