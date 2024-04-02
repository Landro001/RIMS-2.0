# Modulos
import flet
from flet import *
from header import AppHeader

def main(page:Page):
    page.bgcolor = "#F7ECE1"
    page.padding = 20
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader()
            ],
        )
    )
    page.update()
    pass

    


flet.app(target=main)