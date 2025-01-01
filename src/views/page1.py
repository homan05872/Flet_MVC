import flet as ft
from typing import Any

class Page1(ft.View):
    def __init__(self, page:ft.Page, data:dict[str:Any]):
        super().__init__()
        # キャプション設定
        page.title = data['title']
        # レイアウト設定
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        #デザイン設定
        self.bgcolor = "#dcdcdc"
        
        # UI生成
        self.builf_ui()
        
    def builf_ui(self):
        
        # コントローラで使用するUI要素をインスタンス変数で保持
        self.username_input = ft.TextField(label="user", hint_text="ユーザーIDを入力してください。")
        self.password_input = ft.TextField(label="password", hint_text="パスワードを入力してください。")
        self.page1_btn = ft.ElevatedButton("登録", height=40, width=100)
        
        self.controls=[
            ft.Container(
                # デザイン設定
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=300,
                border_radius=10,
                theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
                theme_mode=ft.ThemeMode.DARK,
                bgcolor=ft.colors.SURFACE_VARIANT,
                # UI配置
                content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                    content=ft.Text(
                                                value="登録するユーザー情報を入力してください。",
                                                color="#f8f8ff",
                                                weight=ft.FontWeight.BOLD
                                                ),
                                    margin=ft.margin.only(top=10, bottom=15)
                                    ),
                            self.username_input,
                            self.password_input,
                            ft.Container(content=self.page1_btn, alignment=ft.alignment.center, margin=ft.margin.only(top=30, bottom=10))
                        ],
                    ),
            ),
        ]       
