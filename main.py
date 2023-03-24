from nicegui import ui
import cours_tab
import series_tab


# Homepage
## Header
with ui.header(elevated=True).style('background-color: #282A35;'):
    # ui.button(on_click=lambda: hamburger_menu.toggle()).props('flat color=white icon=menu')
    with ui.tabs() as tabs:
        ui.tab('Cours', icon='book')
        ui.tab('Exercices', icon='code')


## Hamburger menu
# with ui.left_drawer().style('background-color:#282A35;') as hamburger_menu:
#     pass


## Tab content
with ui.tab_panels(tabs, value='Cours').style("width:100%; height:100%;"):
    with ui.tab_panel('Cours'):
        cours_tab.show()
    with ui.tab_panel('Exercices'):
        series_tab.show()


ui.run()
