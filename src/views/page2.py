import flet as ft

class Page2(ft.View):
    def __init__(self, page: ft.Page, data:dict):
        super().__init__()
        self.page = page
        self.data = data
        self.page.title = self.data['title']
        
        # レイアウト設定
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        #デザイン設定
        self.bgcolor = "#dcdcdc"
        if self.data["username"] == "":
            self.data["username"] = "ゲストユーザー"
        
        
        self.build_ui()
        
    def build_ui(self):
        # コントローラで使用するUI要素をインスタンス変数で保持
        self.confirm_pass_btn = ft.IconButton(icon=ft.icons.MESSAGE, tooltip="パスワード確認")
        self.page1_link_btn = ft.IconButton(icon = ft.icons.ARROW_CIRCLE_LEFT, tooltip="ページ1へ戻る", on_click=lambda _:self.page.go("/page1"))
        
        self.controls=[
            ft.Container(
                content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                            value=f"ようこそ！\n{self.data["username"]} さん",
                                            color="#f8f8ff",
                                            weight=ft.FontWeight.BOLD,
                                            size=20,
                                            ),
                                alignment=ft.alignment.center,
                                margin=ft.margin.only(top=10, bottom=15)
                                ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[self.confirm_pass_btn, self.page1_link_btn], 
                                    alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                alignment=ft.alignment.center,
                                margin=ft.margin.only(top=30, bottom=10)
                                )
                        ],
                    ),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=300,
                border_radius=10,
                theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                theme_mode=ft.ThemeMode.DARK,
                bgcolor=ft.colors.SURFACE_VARIANT,
            ),
        ]
        
