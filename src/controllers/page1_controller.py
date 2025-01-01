import flet as ft
from views import Page1
from models import User
from core.base_controller import BaseController


class Page1Controller(BaseController):
    def __init__(self, page: ft.Page):
        super().__init__(page, Page1)
        self.page = page
        self.view = None
        
    def _set_view_event(self):
        self.view.page1_btn.on_click = lambda _ :self.add_user()
        
    def _send_view_data(self):
        return {'title': 'Page1'}
    
    def add_user(self):
        # 入力フォームから値を取得
        User.name = self.view.username_input.value
        User.password = self.view.password_input.value
        
        self.page.go("/page2")
        
    