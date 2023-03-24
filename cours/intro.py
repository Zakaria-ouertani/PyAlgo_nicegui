from nicegui import ui

@ui.page("/Introduction")
def show():
    with ui.header(elevated=True).style("background-color:#282A35;"):
        ui.button(on_click=lambda: ui.open("/")).props("flat color=white icon=home")
    ui.markdown('''
# Introduction
* [L'Algorithme](#L'Algorithme)
* [La Forme Générale d'un Algorithme](#La Forme Générale d'un Algorithme)
* [Les Syntaxes et Structures Algorithmiques](#Les Syntaxes et Structures Algorithmiques]()

## L'Algorithme
### La Forme Générale d'un Algorithme
### Les Syntaxes et Structures Algorithmiques

''')


