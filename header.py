# Header da aplicação

# Modulos
from flet import *
from controls import add_to_control_reference, return_control_reference

# Definir o dicionário retornado como variável no topo da classe
control_map = return_control_reference()

# Classe principal
class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def app_header_instance(self):
        # Função para adicionar a instância da classe em um par chave:valor no dicionário global
        add_to_control_reference("AppHeader", self)

    def app_header_brand(self):
        return Container(
            content= Text(
                "Line Indent",
                size= 15
            )
        )
    
    def app_header_search(self):
        return Container(
            width= 320,
            bgcolor= "white10",
            border_radius= 6,
            opacity= 0,
            animate_opacity= 320,
            padding= 8,
            content= Row(
                spacing= 10,
                vertical_alignment= CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name= icons.SEARCH_ROUNDED,
                        size= 17,
                        opacity= 0.85
                    ),
                    TextField(
                        border_color= "transparent",
                        height= 20,
                        text_size= 14,
                        content_padding= 0,
                        cursor_color= "white",
                        cursor_width= 1,
                        color= "white",
                        hint_text= "Pesquisar"
                    )
                ]
            )
        )
    
    def app_header_storage(self):
        return Container(
            content= IconButton(icons.STORAGE_ROUNDED)
        )

    def show_search_bar(self, e):
        if e.data == "true":
            self.controls[0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
        else:
            self.controls[0].content.controls[1].opacity = 0
            self.controls[0].content.controls[1].content.controls[1].value = ""
            self.controls[0].content.controls[1].update()

    def build(self):
        self.app_header_instance()

        return Container(
            expand= True,
            on_hover= lambda e: self.show_search_bar(e),
            height= 60,
            bgcolor= "#242038",
            border_radius= border_radius.only(top_left= 15, top_right= 15),
            padding= padding.only(left= 15, right= 15),
            content= Row(
                expand= True,
                alignment= MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    self.app_header_brand(),
                    self.app_header_search(),
                    self.app_header_storage(),
                ],
            )
        )
