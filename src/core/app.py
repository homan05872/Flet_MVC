import flet as ft
from controllers import Page1Controller, Page2Controller

class App:
    def __init__(self, page:ft.Page):
        """ アプリの初期化処理(各クラスの連携)

        Args:
            page (ft.Page): アプリのウィンドウを提供するクラス(fletライブラリ)
        """
        self.page:ft.Page = page    # ウィンドウ
        self.route_list:dict = {
            "/page1": Page1Controller(self.page),
            "/page2": Page2Controller(self.page),
        }
        
        # ページ遷移の為のメソッドで設定
        page.on_route_change = self.route_change

    
    def route_change(self, page:ft.Page):
        # 現在のページ表示のクリア
        self.page.views.clear()
        # 次ページのUI生成
        next_conn = self.route_list[page.route]
        next_conn.show()
        # ページ更新
        self.page.update()
        
    def run(self):
        # 初期に表示したいページのURLを指定
        self.page.go("/page1")
        
        
        # # サイドバーの内容
        # sidebar = ft.Column(
        #     [
        #         ft.ElevatedButton("Home", on_click=lambda e: self.page.go("/home")),
        #         ft.ElevatedButton("Profile", on_click=lambda e: self.page.go("/profile")),
        #         ft.ElevatedButton("Settings", on_click=lambda e: self.page.go("/settings")),
        #     ],
        #     alignment=ft.MainAxisAlignment.START,
        #     spacing=10,
        # )
        
        # self.content_area = ft.Column(expand=True)
        
        # # 全体レイアウト
        # self.page.add(
        #     ft.Row(
        #         [
        #             ft.Container(sidebar, width=200, height=self.page.height, bgcolor=ft.Colors.BLUE_100),  # サイドバー
        #             self.content_area  # メインコンテンツエリア
        #         ],
        #         alignment=ft.MainAxisAlignment.START,
        #         spacing=10,
        #     )
        # )