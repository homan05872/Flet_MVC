import flet as ft
from view1 import View1
from view2 import View2

class App:
    def __init__(self, page:ft.Page):
        self.page:ft.Page = page 
        self.views:dict = {
            "/view1": View1,
            "/view2": View2,
        }
        
        page.on_route_change = self.route_change
    
    def route_change(self, handler):
        self.page.views.clear()
        ViewClass = self.views[handler.route]
        view = ViewClass()
        self.page.views.append(view.create(self.page, {'title': 'View1'}))
        self.page.update()
        
    def run(self):
        self.page.go("/view1")


def main(page: ft.Page):
    # ページ切り替え時のロジック
    app = App(page)
    app.run()
    # 初期設定
    # page.title = "Navigation with Modular Views"
    

if __name__ == "__main__":
    ft.app(target=main)