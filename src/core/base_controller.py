import flet as ft
from typing import Any
from abc import ABC, abstractmethod

class BaseController(ABC):
    def __init__(self, page: ft.Page, ViewClass:ft.View):
        self.page = page
        self.ViewClass = ViewClass
        self.view = None
    
    def show(self):
        context = self._send_view_data()
        self.view = self.ViewClass(self.page, context)
        self._set_view_event()
        self.page.views.append(self.view)
    
    @abstractmethod
    def _set_view_event(self) -> None:
        pass
    
    
    @abstractmethod
    def _send_view_data(self) -> dict[str:Any]|None:
        pass