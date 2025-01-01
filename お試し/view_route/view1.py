import flet as ft

class View1:
    
    def create(self, page: ft.Page, data:dict):
        page.title = data['title']
        return ft.View(
            "/view1",
            controls=[
                ft.AppBar(title=ft.Text("View 1"), bgcolor=ft.colors.BLUE),
                ft.TextField(value="View 1"),
                ft.ElevatedButton(
                    "Go to View 2", on_click=lambda _: page.go("/view2")
                ),
            ],
        )
