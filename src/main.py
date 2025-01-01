import flet as ft
from core import App

def main(page: ft.Page):
    # 初期化処理(各クラスの連携)
    app = App(page)
    # 起動
    app.run()

if __name__ == "__main__":
    ft.app(target=main)