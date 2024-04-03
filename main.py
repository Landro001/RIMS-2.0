# Modulos
import flet
from flet import *
from header import AppHeader
from form import AppForm
from data_table import AppDataTable

def main(page:Page):
    page.bgcolor = "#F7ECE1"
    page.padding = 20
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppForm(),
                Column(
                    scroll= "hidden",
                    expand= True,
                    controls=[
                        AppDataTable()
                    ]
                )
            ],
        )
    )
    page.update()
    pass

    


flet.app(target=main)