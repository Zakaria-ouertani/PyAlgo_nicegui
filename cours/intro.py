from nicegui import ui

@ui.page("/Introduction")
def show():
    with ui.header(elevated=True).style("background-color:#282A35;"):
        ui.button(on_click=lambda: ui.open("/")).props("flat color=white icon=home")
