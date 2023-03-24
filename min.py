from nicegui import ui
from cours import intro


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


def show_tab():
    expansion_contents = [
            ["Introduction", intro.show],
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


with ui.header(elevated=True).style('background-color: #282A35;'):
    # ui.button(on_click=lambda: hamburger_menu.toggle()).props('flat color=white icon=menu')
    with ui.tabs() as tabs:
        ui.tab('Cours', icon='book')


with ui.tab_panels(tabs, value='Cours').style("width:100%; height:100%;"):
    with ui.tab_panel('Cours'):
        show_tab()


@ui.page("/Introduction")
def show_i():
    with ui.header(elevated=True).style("background-color:#282A35;"):
        ui.button(on_click=lambda: ui.open("/")).props("flat color=white icon=home")


ui.run()
