# Arquivo principal para manipular entrada dos usuários
from flet import *
from controls import return_control_reference
# from form_helper import FormHelper

#Pega o dicionário do mapa global
control_map = return_control_reference()



def get_input_data(e):
    # Método para tratar os principais dados do usuário
    pass

def return_form_button():
    return Container(
        alignment= alignment.center,
        content= ElevatedButton(
            on_click= lambda e: get_input_data(e),
            bgcolor= "#9067C6",
            color= "white",
            content= Row(
                controls=[
                    Icon(
                        name= icons.ADD_ROUNDED,
                        size= 12,
                    ),
                    Text(
                        "Add Input Field To Table",
                        size= 11,
                        weight= "bold",
                    ),
                ],
            ),
            style= ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius= 6),
                },
                color={
                    "": "white",
                },
            ),
            height= 42,
            width= 220,
        ),
    )
