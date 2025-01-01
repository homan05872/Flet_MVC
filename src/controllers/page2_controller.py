import flet as ft
from views import Page2
from models import User
from typing import Any

from core.base_controller import BaseController

class Page2Controller(BaseController):
    def __init__(self, page: ft.Page):
        super().__init__(page, Page2)
        self.page = page
        self.view:Page2
        
    def _set_view_event(self) -> None:
        self.view.confirm_pass_btn.on_click = lambda _ :self.show_confirm_pass_message()
        
    def _send_view_data(self) -> dict[str:Any]:
        return {
            "title": "Page2",
            "username": User.name,
        }
    
    def show_confirm_pass_message(self):
        
        def close_dialog():
            if self.page.dialog:
                self.page.dialog.open = False
                self.page.update()
        
        # ダイアログを定義
        dlg = ft.AlertDialog(
            title=ft.Text("パスワード確認"),
            content=ft.Text(f"現在のパスワードは: {User.password}"),      
            actions=[
                ft.TextButton("閉じる", on_click=lambda _: close_dialog())
            ]
        )
        # ページにダイアログを設定
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()  # ページを更新してダイアログを反映
    