# Modulos
import flet as ft


# Uma classe final para lidar com dados entre controles
# Dados para preencher a tabela e testar
dummy_data = {
    0: {
        "name": "Apple", 
        "description": "Red and juicy", 
        "quantity": 5, 
        "price": 1.99,
    },
    1: {
        "name": "Bread", 
        "description": "Whole wheat loaf", 
        "quantity": 2, 
        "price": 3.49,
    },
    2: {
        "name": "Milk", 
        "description": "Organic whole milk", 
        "quantity": 1, 
        "price": 2.99,
    },
    3: {
        "name": "Carrot", 
        "description": "Fresh and crunchy", 
        "quantity": 10, 
        "price": 0.99,
    },
    4: {
        "name": "Eggs", 
        "description": "Free-range brown eggs", 
        "quantity": 12, 
        "price": 2.79,
    },
    5: {
        "name": "Chicken", 
        "description": "Boneless skinless breast", 
        "quantity": 2, 
        "price": 7.99,
    },
    6: {
        "name": "Banana", 
        "description": "Ripe and yellow", 
        "quantity": 6, 
        "price": 0.49,
    },
}

class Controller:
    items: dict = dummy_data
    counter: int = len(items)

    @staticmethod
    def get_items():
        return Controller.items
    
    @staticmethod
    def add_item(data: dict):
        Controller.items[Controller.counter] = data
        Controller.counter += 1

# Definição do estilo e dos atributos da classe header
header_style = {
    "height": 60,
    "bgcolor": "#242038",
    "border_radius": ft.border_radius.only(top_left= 15, top_right= 15),
    "padding": ft.padding.only(left= 15, right= 15),
}

# Método que cria e retorna um textfield

def search_field(function: callable):
    return ft.TextField(
        border_color= "transparent",
        height= 20,
        text_size= 14,
        content_padding= 0,
        cursor_color= "white",
        cursor_width= 1,
        color= "white",
        hint_text= "Pesquisar",
        on_change= function,
    )

# Método que adiciona um conteiner no search_field
def search_bar(control: ft.TextField):
    return ft.Container(
        width= 350,
        bgcolor= "white10",
        border_radius= 6,
        opacity= 0,
        animate_opacity= 300,
        padding= 8,
        content= ft.Row(
            spacing= 10,
            vertical_alignment= "center",
            controls=[
                ft.Icon(
                    name= ft.icons.SEARCH_ROUNDED,
                    size= 17,
                    opacity= 0.85,
                ),
                control,
            ],
        ),
    )
    

# Definição da classe header
class Header(ft.Container):
    def __init__(self, dt: ft.DataTable):
        super().__init__(**header_style,
                         on_hover= self.toggle_search
                         )

        # Criando um atributo dados
        self.dt = dt

        # Cria um textfield para pesquisa/filtro
        self.search_value = search_field(self.filter_dt_rows)

        # Cria uma caixa de pesquisa
        self.search = search_bar(self.search_value)

        # Definição de outros atributos da classe
        self.name = ft.Text("R.I.M.S 2.0")
        self.storage = ft.IconButton("storage")

        # Compila os atributos dentro do conteiner do header
        self.content = ft.Row(
            alignment= "spaceBetween",
            controls=[
                self.name,
                self.search,
                self.storage
            ]
        )

    # Define método que alterna a visibilidade da caixa de pesquisa
    def toggle_search(self, e: ft.HoverEvent):
        self.search.opacity = 1 if e.data == "true" else 0
        self.search.update()

    # Define um método placeholder para filtrar os dados
    def filter_dt_rows(self, e):
        # Filtra os dados com base nos caracteres da caixa de pesquisa
        for data_rows in self.dt.rows:
            # Filtrando com base na coluna um
            # apenas a primeira posição do índice [0]
            data_cell = data_rows.cells[0]
            # Alterando a visibilidade em relação ao que está sendo digitado na caixa de pesquisa
            # Lidando com distinção de maiúsculas e minúsculas, definindo tudo como minúsculo
            data_rows.visible = (
                True if e.control.value.lower() in data_cell.content.value.lower()
                else False
            )

            data_rows

# Define o estilo e atributos da classe Form 
form_style = {
    "border_radius": 8,
    "border": ft.border.all(1, "#EBEBEB"),
    "bgcolor": "white10",
    "padding": 15,
}

# Define o método que cria e retorna um textfield
def text_field():
    return ft.TextField(
        border_color= "transparent",
        height= 20,
        text_size= 13,
        content_padding= 0,
        cursor_color= "black",
        cursor_width= 1,
        cursor_height= 18,
        color= "black"
    )

# Define um contêiner para envolver o textfield
def text_field_container(
        expand: bool | int, name: str, control: ft.TextField
):
    return ft.Container(
        expand= expand,
        height= 45,
        bgcolor= "#EBEBEB",
        border_radius= 6,
        padding= 8,
        content= ft.Column(
            spacing= 1,
            controls= [
                ft.Text(
                    value= name,
                    size= 9,
                    color= "black",
                    weight= "bold"
                ),
                control
            ]
        )
    )

# Definição a classe Form
class Form(ft.Container):
    def __init__(self, dt: ft.DataTable):
        super().__init__(**form_style)

        # Criando um atributo dados
        self.dt = dt

        # Definição das 4 linhas textfields
        self.row1_value = text_field()
        self.row2_value = text_field()
        self.row3_value = text_field()
        self.row4_value = text_field()
        
        # Define e envolve cada um dentro de um contêiner
        self.row1 = text_field_container(
            True, "Row One", self.row1_value
        )
        self.row2 = text_field_container(
            3, "Row Two", self.row2_value
        )
        self.row3 = text_field_container(
            1, "Row Three", self.row3_value
        )
        self.row4 = text_field_container(
            1, "Row Four", self.row4_value
        )

        # Definição de um botão para enviar os dados
        self.submit = ft.ElevatedButton(
            text= "Enviar",
            style= ft.ButtonStyle(shape={
                "": ft.RoundedRectangleBorder(radius= 8)
            }),
            on_click= self.submit_data,
        )

        # Compila todos os atributos em um conteiner de classe
        self.content = ft.Column(
            expand= True,
            controls=[
                ft.Row(controls=[self.row1]),
                ft.Row(controls=[self.row2, self.row3, self.row4]),
                ft.Row(controls=[self.submit], alignment= "end"),
            ]
        )

    # Método para envio dos dados
    def submit_data(self, e: ft.TapEvent):
        # Obtemos o valor de cada campo de texto e criamos uma estrutura de dados para ele
        data = {
            "col1": self.row1_value.value,
            "col2": self.row2_value.value,
            "col3": self.row3_value.value,
            "col4": self.row4_value.value,
        }

        # Chamamos o controlador e adicionamos os dados ao seu ditado de itens
        Controller.add_item(data)

        # Limpa as entradas e preenche novamente a tabela de dados
        self.clear_entries()
        self.dt.fill_data_table()

    # Método para limpar todas as entradas pós-envio
    def clear_entries(self):
        self.row1_value.value = ""
        self.row2_value.value = ""
        self.row3_value.value = ""
        self.row4_value.value = ""

        self.content.update()

# Defnição alguns estilos, atributos e colunas da tabela de dados
column_names = [
    "Column One", "Column Two", "Column Three", "Column Four"
]

data_table_style = {
    "expand": True,
    "border_radius": 8,
    "border": ft.border.all(2, "#EBEBEB"),
    "horizontal_lines": ft.border.BorderSide(1, "#EBEBEB"),
    "columns": [
        # Usando list comprehension para criar as colunas de dados
        ft.DataColumn(ft.Text(index, size= 12, color= "black", weight= "bold"))
        for index in column_names
    ]
}

# Definição da classe para a tabela de dados
class DataTable(ft.DataTable):
    def __init__(self):
        super().__init__(**data_table_style)
        # Criando um atributo que pega os items
        self.df = Controller.get_items()

    def fill_data_table(self):
        # Limpa as linhas da tabela de dados para lote novo/atualizado
        self.rows = []
        # Verifica o tipo de dados dict para entender o seguinte loop
        for values in self.df.values():
            # Cria um novo DataRow
            data = ft.DataRow()
            data.cells = [
                ft.DataCell(
                    ft.Text(value, color= "black")
                ) for value in values.values()
            ]

            self.rows.append(data)
        
        self.update()

def main(page: ft.Page):
    page.bgcolor = "#FDFDFD"

    table = DataTable()
    header = Header(dt= table)
    form = Form(dt= table)
    

    page.add(
        ft.Column(
            expand= True,
            controls=[
                # Header...
                header,
                ft.Divider(height= 2, color="transparent"),      
                # Form...
                form,
                ft.Column(
                    scroll= "hidden",
                    expand= True,
                    controls= [ft.Row(controls=[table])] # Table
                )
            ]
        )
    )
    
    
    page.update()
    table.fill_data_table()

ft.app(target=main)
