# Modulos
import flet
from flet import *
import sqlite3

def main(page:Page):
    page.bgcolor = "#F7ECE1"
    page.padding = 20
    page.add(
        Column(
            expand=True,
            controls=[

            ],
        )
    )
    page.update()
    pass

    


flet.app(target=main)