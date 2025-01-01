import flet as ft

class View2:
    
    def create(self, page: ft.Page, data:dict):
        page.title = data['title']
        return ft.View(
            "/view2",
            controls=[
                ft.AppBar(title=ft.Text("View 2"), bgcolor=ft.colors.RED),
                ft.TextField(value="View 2"),
                ft.ElevatedButton(
                    "Go to View 1", on_click=lambda _: page.go("/view1")
                ),
            ],
        )
